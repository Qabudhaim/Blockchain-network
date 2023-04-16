from fastapi import FastAPI, Request
from blockchain import Blockchain
from fastapi.encoders import jsonable_encoder
from typing import Dict, Union
from fastapi.templating import Jinja2Templates
import uuid
import httpx
import asyncio
from pydantic import BaseModel, conlist

app = FastAPI()
templates = Jinja2Templates(directory="templates")
blockchain = Blockchain()

@app.get("/")
async def root():
    return {"message": f"Node {blockchain.url}"}

@app.get("/blockchain")
async def get_blockchain():
    return jsonable_encoder(blockchain)

@app.post("/add_transaction")
async def create_transaction(data: Dict):
    new_transaction = data.get("transaction")
    if new_transaction['sender'] is None or new_transaction['recipient'] is None or new_transaction['amount'] is None:
        return {"error": "Missing values"}

    new_transaction = blockchain.create_new_transaction(**new_transaction)
    block_index = blockchain.add_transaction_to_pending_transactions(new_transaction)
    return {"message": f"Transaction will be add to block {block_index}"}

@app.post("/add_transaction/broadcast")
async def broadcast_transaction(data: Dict[str, Union[int, str]]):
    sender = data.get("sender")
    recipient = data.get("recipient")
    amount = data.get("amount")
    if sender is None or recipient is None or amount is None:
        return {"error": "Missing values"}
    
    new_transaction = blockchain.create_new_transaction(sender, recipient, amount)
    blockchain.add_transaction_to_pending_transactions(new_transaction)

    tasks = []
    for node in blockchain.network_nodes:
        task = asyncio.create_task(make_request(f"{node}/add_transaction", {'transaction': new_transaction.dict()}))
        tasks.append(task)
    await asyncio.gather(*tasks)
    
    return {"message": f"Transaction created and broadcast successfully"}

@app.get("/mine")
async def mine():
    last_block = blockchain.last_block
    previous_hash = last_block['hash']
    block_data = {
        'transactions': blockchain.pending_transactions,
        'index': len(blockchain.chain) + 1,
    }
    nonce = blockchain.proof_of_work(block_data, previous_hash)
    hash = blockchain.hash_block(block_data, previous_hash, nonce)

    block = blockchain.create_new_block(nonce = nonce, hash = hash, previous_hash = previous_hash)

    tasks = []
    for node in blockchain.network_nodes:
        task = asyncio.create_task(make_request(f"{node}/receive-new-block", {"block": block.dict()}))
        tasks.append(task)
    await asyncio.gather(*tasks)

    transaction = blockchain.create_new_transaction("10000000000000000000000000000001", blockchain.address, 5)

    task = asyncio.create_task(make_request(f"{blockchain.url}/add_transaction/broadcast", transaction.dict()))
    await asyncio.gather(*tasks)

    block = jsonable_encoder(block)
    result = {
        "Message": "Block was mined successfully",
        "Block": block
    }
    return result

@app.post("/receive-new-block")
async def receive_new_block(data: Dict):
    new_block = data.get('block')
    last_block = blockchain.last_block
    if (last_block['hash'] == new_block['previous_hash'] and last_block['index'] + 1 == new_block['index']):
        blockchain.chain.append(new_block)
        blockchain.pending_transactions = []
        return {"message": "Block accepted"}
    return {"error": "Block rejected"}
    
@app.post("/register-and-broadcast-node")
async def register_and_broadcast_node(data: Dict[str, str]):
    new_node = data.get("url")
    if (new_node in blockchain.network_nodes or new_node == blockchain.url):
        return {"error": "Node already exsist"}

    blockchain.network_nodes.append(new_node)

    tasks = []
    for node in blockchain.network_nodes:
        task = asyncio.create_task(make_request(f"{node}/register-node", {"url": new_node}))
        tasks.append(task)
    await asyncio.gather(*tasks)

    task = asyncio.create_task(make_request(f"{new_node}/register-nodes-bulk", {"network_nodes": [blockchain.url, *blockchain.network_nodes]}))
    await asyncio.gather(*tasks)

    return {"message": "Node registered successfully"}

@app.post("/register-node")
async def register_node(data: Dict[str, str]):
    url = data.get("url")
    if (url in blockchain.network_nodes or url == blockchain.url):
        return {"error": "Node already exsist"}
    
    blockchain.network_nodes.append(url)
    return {"Message": "Node added successfuly",}

@app.post("/register-nodes-bulk")
async def register_nodes_bulk(data: Dict[str, list]):
    network_nodes = data.get("network_nodes")
    for node in network_nodes:
        if (node in blockchain.network_nodes or node == blockchain.url):
            return {"error": "Node already exsist"}
        blockchain.network_nodes.append(node)

    return {"message": "Bulk registration successful."}

@app.get("/consensus")
async def consensus():
    tasks = []
    for node in blockchain.network_nodes:
        task = asyncio.create_task(make_request(f"{node}/blockchain", requst_type="GET"))
        tasks.append(task)
    responses = await asyncio.gather(*tasks)

    # return {'responses': [response.json() for response in responses]}

    max_length = len(blockchain.chain)
    new_chain = None
    pending_transactions = []

    for response in responses:
        chain = response.json().get("chain")
        length = len(chain)
        if (length > max_length and blockchain.chain_is_valid(chain)):
            max_length = length
            new_chain = chain
            pending_transactions = response.json().get("pending_transactions")

    if new_chain:
        blockchain.chain = new_chain
        blockchain.pending_transactions = pending_transactions
        return {"message": "Chain replaced", "new_chain": blockchain.chain}
    return {"message": "Chain is authoritative", "chain": blockchain.chain}
    
@app.get("/search_block/{block_hash}")
async def search_block(request: Request):
    block = blockchain.get_block(block_hash=request.path_params["block_hash"])
    if block:
        return {"block": block}
    return {"error": "Block not found"}

@app.get("/search_transaction/{transaction_id}")
async def search_transaction(request: Request):
    transaction = blockchain.get_transaction(transaction_id=request.path_params["transaction_id"])
    if transaction:
        return {"transaction": transaction}
    return {"error": "Transaction not found"}

@app.get("/search_address/{address}")
async def search_address(request: Request):
    transactions = blockchain.get_address(address=request.path_params["address"])
    if transactions:
        return {"transactions": transactions}
    return {"error": "Address not found"}

@app.get("/test")
async def index(request: Request):
    context = {"title": "FastAPI Demo", "message": "Hello, World!"}
    return templates.TemplateResponse("index.html", {"request": request, **context})
          
async def make_request(url, data={}, requst_type="POST"):
    async with httpx.AsyncClient() as client:
        if requst_type == "GET":
            response = await client.get(url)
        else:
            response = await client.post(url, json=data)
        return response