from fastapi import FastAPI
from blockchain import Blockchain
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/blockchain")
async def blockchain():
    blockchain = Blockchain()
    blockchain.create_new_block(nonce = 200, hash = '00', previous_hash ='00')
    blockchain.create_new_block(nonce = 300, hash = '000', previous_hash ='000')
    blockchain = jsonable_encoder(blockchain)
    return blockchain
