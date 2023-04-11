import pytest
from blockchain import Blockchain

def test_genesis_block():
    blockchain = Blockchain()
    assert blockchain.genesis_block == blockchain.chain[0]
    assert blockchain.genesis_block['nonce'] == 100
    assert blockchain.genesis_block['hash'] == '0'
    assert blockchain.genesis_block['previous_hash'] == '0'
    
def test_hash_block():
    blockchain = Blockchain()
    block_data = {
        'transactions': blockchain.pending_transactions,
        'index': len(blockchain.chain) + 1,
    }
    assert blockchain.hash_block(block_data, 14401) == '0000858bccdc4c1a8d8288e1a15bf6b55c4c3646f32b86e95e0210e04529a1b5'

def test_proof_of_work():
    blockchain = Blockchain()
    block = blockchain.last_block
    block['timestamp'] = 0
    assert blockchain.proof_of_work(block) == 215711

if __name__ == '__main__':
    pytest.main([__file__])