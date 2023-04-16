from blockchain import Blockchain

blockchain = Blockchain()

chains = [
  [
    {
      "index": 1,
      "timestamp": 1681654764,
      "transactions": [],
      "nonce": 100,
      "previous_hash": "0",
      "hash": "0"
    },
    {
      "index": 2,
      "timestamp": 1681654791,
      "transactions": [
        {
          "sender": "Qusai",
          "recipient": "test",
          "amount": 1234,
          "timestamp": 1681654787,
          "transaction_id": "a61151c3fb974b7a8b84f64759ed9959"
        },
        {
          "sender": "Qusai",
          "recipient": "test",
          "amount": 1234,
          "timestamp": 1681654788,
          "transaction_id": "640c7474d5ec45bc8c78b8b3d253f236"
        }
      ],
      "nonce": 2324,
      "previous_hash": "0",
      "hash": "0000bc8df154955e5249bc358017105c9c426c08f6d2efe2f81e58e73e5b72b0"
    },
    {
      "index": 3,
      "timestamp": 1681654804,
      "transactions": [
        {
          "sender": "10000000000000000000000000000001",
          "recipient": "48ead08a963c4a80ae83ccba74ea6ebd",
          "amount": 5,
          "timestamp": 1681654791,
          "transaction_id": "73fcb2f2868f4e3a924491d0b430f17c"
        }
      ],
      "nonce": 83146,
      "previous_hash": "0000bc8df154955e5249bc358017105c9c426c08f6d2efe2f81e58e73e5b72b0",
      "hash": "0000c63e4d18cfd0a7fc58f3d770e6bea26cbb8b1e28695ef0bdcf19a4ce3f91"
    },
    {
      "index": 4,
      "timestamp": 1681654813,
      "transactions": [
        {
          "sender": "10000000000000000000000000000001",
          "recipient": "48ead08a963c4a80ae83ccba74ea6ebd",
          "amount": 5,
          "timestamp": 1681654804,
          "transaction_id": "9e4f8c62d08a4663a03197f1452ebf83"
        }
      ],
      "nonce": 26859,
      "previous_hash": "0000c63e4d18cfd0a7fc58f3d770e6bea26cbb8b1e28695ef0bdcf19a4ce3f91",
      "hash": "000053aef6fcd4d909cafd686de7fcc3d854f1e87186c0371c29d348e31a141e"
    }
  ],
  [
    {
      "index": 1,
      "timestamp": 1681654767,
      "transactions": [],
      "nonce": 100,
      "previous_hash": "0",
      "hash": "0"
    },
    {
      "index": 2,
      "timestamp": 1681654791,
      "transactions": [
        {
          "sender": "Qusai",
          "recipient": "test",
          "amount": 1234,
          "timestamp": 1681654787,
          "transaction_id": "a61151c3fb974b7a8b84f64759ed9959"
        },
        {
          "sender": "Qusai",
          "recipient": "test",
          "amount": 1234,
          "timestamp": 1681654788,
          "transaction_id": "640c7474d5ec45bc8c78b8b3d253f236"
        }
      ],
      "nonce": 2324,
      "previous_hash": "0",
      "hash": "0000bc8df154955e5249bc358017105c9c426c08f6d2efe2f81e58e73e5b72b0"
    },
    {
      "index": 3,
      "timestamp": 1681654804,
      "transactions": [
        {
          "sender": "10000000000000000000000000000001",
          "recipient": "48ead08a963c4a80ae83ccba74ea6ebd",
          "amount": 5,
          "timestamp": 1681654791,
          "transaction_id": "73fcb2f2868f4e3a924491d0b430f17c"
        }
      ],
      "nonce": 83146,
      "previous_hash": "0000bc8df154955e5249bc358017105c9c426c08f6d2efe2f81e58e73e5b72b0",
      "hash": "0000c63e4d18cfd0a7fc58f3d770e6bea26cbb8b1e28695ef0bdcf19a4ce3f91"
    },
    {
      "index": 4,
      "timestamp": 1681654813,
      "transactions": [
        {
          "sender": "10000000000000000000000000000001",
          "recipient": "48ead08a963c4a80ae83ccba74ea6ebd",
          "amount": 5,
          "timestamp": 1681654804,
          "transaction_id": "9e4f8c62d08a4663a03197f1452ebf83"
        }
      ],
      "nonce": 26859,
      "previous_hash": "0000c63e4d18cfd0a7fc58f3d770e6bea26cbb8b1e28695ef0bdcf19a4ce3f91",
      "hash": "000053aef6fcd4d909cafd686de7fcc3d854f1e87186c0371c29d348e31a141e"
    }
  ],
  [
    {
      "index": 1,
      "timestamp": 1681654770,
      "transactions": [],
      "nonce": 100,
      "previous_hash": "0",
      "hash": "0"
    },
    {
      "index": 2,
      "timestamp": 1681654791,
      "transactions": [
        {
          "sender": "Qusai",
          "recipient": "test",
          "amount": 1234,
          "timestamp": 1681654787,
          "transaction_id": "a61151c3fb974b7a8b84f64759ed9959"
        },
        {
          "sender": "Qusai",
          "recipient": "test",
          "amount": 1234,
          "timestamp": 1681654788,
          "transaction_id": "640c7474d5ec45bc8c78b8b3d253f236"
        }
      ],
      "nonce": 2324,
      "previous_hash": "0",
      "hash": "0000bc8df154955e5249bc358017105c9c426c08f6d2efe2f81e58e73e5b72b0"
    },
    {
      "index": 3,
      "timestamp": 1681654804,
      "transactions": [
        {
          "sender": "10000000000000000000000000000001",
          "recipient": "48ead08a963c4a80ae83ccba74ea6ebd",
          "amount": 5,
          "timestamp": 1681654791,
          "transaction_id": "73fcb2f2868f4e3a924491d0b430f17c"
        }
      ],
      "nonce": 83146,
      "previous_hash": "0000bc8df154955e5249bc358017105c9c426c08f6d2efe2f81e58e73e5b72b0",
      "hash": "0000c63e4d18cfd0a7fc58f3d770e6bea26cbb8b1e28695ef0bdcf19a4ce3f91"
    },
    {
      "index": 4,
      "timestamp": 1681654813,
      "transactions": [
        {
          "sender": "10000000000000000000000000000001",
          "recipient": "48ead08a963c4a80ae83ccba74ea6ebd",
          "amount": 5,
          "timestamp": 1681654804,
          "transaction_id": "9e4f8c62d08a4663a03197f1452ebf83"
        }
      ],
      "nonce": 26859,
      "previous_hash": "0000c63e4d18cfd0a7fc58f3d770e6bea26cbb8b1e28695ef0bdcf19a4ce3f91",
      "hash": "000053aef6fcd4d909cafd686de7fcc3d854f1e87186c0371c29d348e31a141e"
    }
  ]
]

mined_version = [
    {
  "Message": "Block was mined successfully",
  "Block": {
    "index": 6,
    "timestamp": 1681654026,
    "transactions": [
      {
        "sender": "10000000000000000000000000000001",
        "recipient": "dc68f8a1a26449a881dfbfc884437b02",
        "amount": 5,
        "timestamp": 1681653918,
        "transaction_id": "b13fdf88a8ae4d64bf7a264a0c978681"
      }
    ],
    "nonce": 12968,
    "previous_hash": "0000b7ea366c6af505f91abe55d40d158ea904a095a0fc4120e29b49cbbdbdfd",
    "hash": "0000b1f60222c973a9051086d6626d1bcc82ed3c05fc1a8cacb660fe5768a30c"
  },
  "Hash_data": {
    "block_data": {
      "transactions": [
        {
          "sender": "10000000000000000000000000000001",
          "recipient": "dc68f8a1a26449a881dfbfc884437b02",
          "amount": 5,
          "timestamp": 1681653918,
          "transaction_id": "b13fdf88a8ae4d64bf7a264a0c978681"
        }
      ],
      "index": 6
    },
    "previous_hash": "0000b7ea366c6af505f91abe55d40d158ea904a095a0fc4120e29b49cbbdbdfd",
    "nonce": 12968
  }
}
]

for chain in chains:
    print(blockchain.chain_is_valid(chain))
    print('********')

hash_data = {
    "block_data": {
      "transactions": [
        {
          "sender": "10000000000000000000000000000001",
          "recipient": "806a435143ae4338b438e1e3175923fb",
          "amount": 5,
          "timestamp": 1681652676,
          "transaction_id": "775ac872910c42da8792c838e4dbb598"
        }
      ],
      "index": 3
    },
    "previous_hash": "0000e3f975ef46ddf1957104e0720f9bada324aeee0258eb206ce434711b5e1c",
    "nonce": 30099
  }

c = blockchain.hash_block(hash_data["block_data"], hash_data["previous_hash"], hash_data["nonce"])
print(c)