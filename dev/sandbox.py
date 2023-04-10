from blockchain import Blockchain
import hashlib
import json

blockchain = Blockchain()

print(blockchain.genesis_block)

print(blockchain.last_block)

blockchain.create_new_transaction('ASDFKLASJFDASDFLKAJSDF', 'ASDFKLASJFDASDFLKAJSDF', 150)

print(blockchain.pending_transactions)
print(blockchain.__dict__)

print("********")

blockchain.last_block['timestamp'] = 0

block_string = json.dumps(blockchain.last_block, sort_keys=True)
print(block_string)

nonce = 0
data = block_string + str(nonce)
HashedBlock = hashlib.sha256(data.encode()).hexdigest()

while(HashedBlock[:4] != '0000'):
    nonce += 1
    data = block_string + str(nonce)
    HashedBlock = hashlib.sha256(data.encode()).hexdigest()

    print(HashedBlock)

print("********")
print(HashedBlock)
print(nonce)


