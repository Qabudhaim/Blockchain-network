from fastapi import FastAPI, Request
from blockchain import Blockchain
from fastapi.encoders import jsonable_encoder
from typing import Dict, Union
from fastapi.templating import Jinja2Templates
from time import time
import uuid
import httpx
import asyncio

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
def create_transaction(data: Dict[str, Union[int, str]]):
    sender = data.get("sender")
    recipient = data.get("recipient")
    amount = data.get("amount")
    if sender is None or recipient is None or amount is None:
        return {"error": "Missing values"}

    new_transaction = blockchain.create_new_transaction(sender, recipient, amount)
    return new_transaction

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

    blockchain.pending_transactions.append({
        "sender": "00000000000000000000000000000000",
        "recipient": blockchain.address,
        "amount": 5,
        "timestamp": int(time()),
        "transaction_id": str(uuid.uuid4()).replace('-', ''),
    })

    block = jsonable_encoder(block)
    result = {
        "Message": "Block was mined successfully",
        "Block": block
    }
    return result


    
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
    
@app.get("/test")
async def index(request: Request):
    context = {"title": "FastAPI Demo", "message": "Hello, World!"}
    return templates.TemplateResponse("index.html", {"request": request, **context})
          
async def make_request(url, data):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
        return response