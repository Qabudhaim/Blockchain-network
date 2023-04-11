from fastapi import FastAPI
from blockchain import Blockchain
from fastapi.encoders import jsonable_encoder
from typing import Dict

app = FastAPI()
blockchain = Blockchain()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/blockchain")
async def get_blockchain():
    blockchain_json = jsonable_encoder(blockchain)
    return blockchain_json

@app.get("/mine")
async def mine():
    block = blockchain.create_new_block(nonce = 200, hash = '00', previous_hash ='00')
    block = jsonable_encoder(block)
    result = {
        "Message": "Block was mined successfully",
        "Block": block
    }
    return result

@app.post("/add_transaction")
def create_transaction(data: Dict[str, str]):
    sender = data.get("sender")
    recipient = data.get("recipient")
    amount = data.get("amount")
    if sender is None:
        return {"error": "No sender specified"}

    new_transaction = blockchain.create_new_transaction(sender, recipient, amount)
    return new_transaction