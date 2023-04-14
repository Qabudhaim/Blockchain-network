from pydantic import BaseModel, validator, conlist, constr, conint # Constraint integer
from time import time
from enum import Enum
from typing import Optional
import uuid

class Transaction(BaseModel):
    sender: str
    recipient: str
    amount: int
    timestamp: int
    transaction_id: str

class Block(BaseModel):
    index: int
    timestamp: int
    transactions: conlist(Transaction, min_items=1)
    nonce: int
    previous_hash: str
    hash: str

transaction = Transaction(
    sender="Qusai",
    recipient="Tareq",
    amount=100,
    timestamp=int(time()),
    transaction_id=str(uuid.uuid4()).replace('-', ''),
)

block = Block(
    index=1,
    timestamp=int(time()),
    transactions=[transaction],
    nonce=100,
    previous_hash="0",
    hash="0",
)

print(block.json())
print(transaction.json())

