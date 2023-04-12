from fastapi import FastAPI, Request
from blockchain import Blockchain
from fastapi.encoders import jsonable_encoder
from typing import Dict, Union
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
blockchain = Blockchain()

@app.get("/")
async def root():
    return {"message": f"Node {blockchain.address}"}

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
        "recipient": "Node_Address",
        "amount": 12.5
    })

    block = jsonable_encoder(block)
    result = {
        "Message": "Block was mined successfully",
        "Block": block
    }
    return result

@app.get("/register-and-broadcast-node")
async def root():
    return {"message": "register-and-broadcast-node"}

@app.get("/register-node")
async def root():
    return {"message": "register-node"}

@app.get("/register-nodes-bulk")
async def root():
    return {"message": "register-nodes-bulk"}
    
@app.get("/test")
async def index(request: Request):
    context = {"title": "FastAPI Demo", "message": "Hello, World!"}
    return templates.TemplateResponse("index.html", {"request": request, **context})
    
      
