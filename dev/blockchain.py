import hashlib
import json
from time import time
import uuid
import os
from pydantic import BaseModel, conlist
from typing import Optional

class Transaction(BaseModel):
    sender: str
    recipient: str
    amount: int
    timestamp: int
    transaction_id: str

class Block(BaseModel):
    index: int
    timestamp: int
    transactions: Optional[conlist(Transaction)]
    nonce: int
    previous_hash: str
    hash: str

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.address = str(uuid.uuid4()).replace('-', '')
    
        self.url = 'http://172.17.0.1:' + os.environ.get("ADDRESS", "8080")
        self.network_nodes = []
        
        # Create the genesis block
        self.create_new_block(nonce = 100, hash = '0', previous_hash ='0')

    def create_new_block(self, nonce, hash, previous_hash=None):
        # Creates a new Block and adds it to the chain
        block = Block(
            index=len(self.chain) + 1,
            timestamp=int(time()),
            transactions=self.pending_transactions,
            nonce=nonce,
            previous_hash=previous_hash,
            hash=hash,
        )
        # block = {
        #     'index': len(self.chain) + 1,
        #     'timestamp': int(time()),
        #     'transactions': self.pending_transactions,
        #     'nonce': nonce,
        #     'previous_hash': previous_hash,
        #     'hash': hash,
        # }

        # Reset the current list of transactions
        self.pending_transactions = []

        self.chain.append(block.dict())
        return block
    
    def create_new_transaction(self, sender, recipient, amount, timestamp=None, transaction_id=None):
        # Adds a new transaction to the list of transactions
        new_transaction = Transaction(
            sender=sender,
            recipient=recipient,
            amount=amount,
            timestamp= timestamp or int(time()),
            transaction_id= transaction_id or str(uuid.uuid4()).replace('-', ''),
        )
        # new_transaction = {
        #     'sender': sender,
        #     'recipient': recipient,
        #     'amount': amount,
        #     'timestamp': int(time()),
        #     'transaction_id': str(uuid.uuid4()).replace('-', ''),
        # }

        return new_transaction
    
    def add_transaction_to_pending_transactions(self, transaction):
        self.pending_transactions.append(transaction.dict())
        return self.last_block['index'] + 1 # Return in which block the transaction will be added
    
    @staticmethod
    def hash_block(block_data, previous_hash, nonce):
        block_string = json.dumps(block_data, sort_keys=True)
        data = block_string + previous_hash + str(nonce)
        hash = hashlib.sha256(data.encode()).hexdigest()

        return hash
    
    def proof_of_work(self, block_data, previous_hash):
        nonce = 0
        hash = self.hash_block(block_data, previous_hash, nonce)
        while(self.proof_is_valid(hash) is False):
            nonce += 1
            hash = self.hash_block(block_data, previous_hash, nonce)

        return nonce
    
    def chain_is_valid(self, chain):
        valid_chain = True

        # Check if the genesis block is correct
        genesis_block = chain[0]
        correct_nonce = genesis_block['nonce'] == 100
        correct_previous_hash = genesis_block['previous_hash'] == "0"
        correct_hash = genesis_block['hash'] == "0"
        correct_transactions = genesis_block['transactions'] == []

        if (not correct_nonce or not correct_previous_hash or not correct_hash or not correct_transactions):
            valid_chain = False
        
        # Check if the hash of the block is correct
        for i in range(1, len(chain)):
            current_block = chain[i]
            previous_block = chain[i-1]
            block_hash = self.hash_block(
                {'transactions': current_block['transactions'], 'index': current_block['index']}, 
                previous_block['hash'], 
                current_block['nonce']
                )
               
            if block_hash[:4] != "0000":
                valid_chain = False
                break
            
            if current_block['previous_hash'] != previous_block['hash']:
                valid_chain = False
                break
            
        return valid_chain

    def get_block(self, block_hash):
        # Search for the block with the given hash
        # Returns None if no block is found
        for block in self.chain:
            if block['hash'] == block_hash:
                return block
        return None
    
    def get_transaction(self, transaction_id):
        # Search for the transaction with the given id
        # Returns None if no transaction is found
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction['transaction_id'] == transaction_id:
                    return transaction
        return None
    
    def get_address(self, address):
        address_transactions = []
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction['recipient'] == address or transaction['sender'] == address:
                    address_transactions.append(transaction)
        
        return address_transactions

    @property
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]
    
    @property
    def genesis_block(self):
        # Returns the first Block in the chain
        return self.chain[0]

    @staticmethod
    def proof_is_valid(hash):
        return hash[:4] == "0000"
