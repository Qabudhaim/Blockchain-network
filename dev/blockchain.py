import hashlib
import json
from time import time
import uuid
import os

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.address = str(uuid.uuid4()).replace('-', '')
    
        self.url = 'http://localhost:' + os.environ.get("ADDRESS", "8080")
        self.network_nodes = []
        
        # Create the genesis block
        self.create_new_block(nonce = 100, hash = '0', previous_hash ='0')

    def create_new_block(self, nonce, hash, previous_hash=None):
        # Creates a new Block and adds it to the chain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': int(time()),
            'transactions': self.pending_transactions,
            'nonce': nonce,
            'previous_hash': previous_hash,
            'hash': hash,
        }

        # Reset the current list of transactions
        self.pending_transactions = []

        self.chain.append(block)
        return block
    
    def create_new_transaction(self, sender, recipient, amount):
        # Adds a new transaction to the list of transactions
        new_transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'timestamp': int(time()),
            'transaction_id': str(uuid.uuid4()).replace('-', ''),
        }

        self.pending_transactions.append(new_transaction)
        return new_transaction
    
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
    
    # def register_node(self, address):
    #     # Add a new node to the list of nodes
    #     parsed_url = urlparse(address)
    #     self.nodes.add(parsed_url.netloc)

    # def valid_chain(self, chain):
    #     # Determine if a given blockchain is valid
    #     last_block = chain[0]
    #     current_index = 1

    #     while current_index < len(chain):
    #         block = chain[current_index]
    #         print(f'{last_block}')
    #         print(f'{block}')
    #         print("-----------")
    #         # Check that the hash of the block is correct
    #         if block['previous_hash'] != self.hash(last_block):
    #             return False

    #         # Check that the Proof of Work is correct
    #         if not self.valid_proof(last_block['proof'], block['proof']):
    #             return False

    #         last_block = block
    #         current_index += 1

    #     return True
    
    # def resolve_conflicts(self):
    #     # This is our Consensus Algorithm, it resolves conflicts
    #     # by replacing our chain with the longest one in the network.
    #     neighbours = self.nodes
    #     new_chain = None

    #     # We're only looking for chains longer than ours
    #     max_length = len(self.chain)

    #     # Grab and verify the chains from all the nodes in our network
    #     for node in neighbours:
    #         response = requests.get(f'http://{node}/chain')

    #         if response.status_code == 200:
    #             length = response.json()['length']
    #             chain = response.json()['chain']

    #             # Check if the length is longer and the chain is valid
    #             if length > max_length and self.valid_chain(chain):
    #                 max_length = length
    #                 new_chain = chain

    #     # Replace our chain if we discovered a new, valid chain longer than ours
    #     if new_chain:
    #         self.chain = new_chain
    #         return True

    #     return False
