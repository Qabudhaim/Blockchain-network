# Blockchain network

## Tech stack

- FastAPI
- Docker
- ReactJS
- TailwindCSS

## How to run

Download the project and run the following commands in the root directory:

1. Create a Docker network
`docker network create blockchain_network`
The default ip range for Docker network is 172.17.0.0/16, run ipconfig(Windows)/ifconfig(Linux) to check your ip address and make sure it is in the range.

2. Build Docker images
`sudo docker build -t blockchain .`

3. Run Docker containers
`sudo docker run --env ADDRESS=81 --network=blockchain_network -p 81:80 blockchain`

    **NOTE:** Make sure ADDRESS and port number are the same.

4. Open your browser and go to http://localhost:81

5. You can also run multiple nodes by changing the port number and ADDRESS environment variable.

## How to use

I will assume the port number is 81.

- You can add a transaction by sending a POST request to http://localhost:81/add_transaction/broadcast

    The body of the request looks like this:

    ```json
    {
        "sender": "b9c67db94d7d4d339a577d9427869e5c", 
        "recipient": "e034d9cc327b4fcdae8f3ed30442f04d",
        "amount": 5
    }
    ```

    The transaction will be broadcasted to all nodes in the network.

- You can mine a block by sending a GET request to http://localhost:81/mine

- You can get the blockchain by sending a GET request to http://localhost:81/blockchain

- You can register a node by sending a POST request to http://localhost:83/register-and-broadcast-node

    The body of the request looks like this:

    ```json
    {
        "url": "http://172.17.0.1:83"
    }
    ```

    The node will be broadcasted to all nodes in the network.

- The new node can be synchronized by sending a GET request to http://localhost:83/consensus

- Explore the blockchain by navigating to http://localhost:81/explore

    ![Alt text](dev/block_explorer.png "Block explorer")

    Blocks can be explored by searching for the block hash.
    Transactions can be explored by searching for the transaction id.
    And addresses can be explored by searching for the address, where all the transactions related to that address will be displayed in addition to address's balance.

## APIs list

FastAPI provides a Swagger UI for the API documentation, you can access it by navigating to http://localhost:81/docs

User APIs:

- GET /blockchain
- GET /mine
- GET /consensus
- GET /explore
- POST /register-and-broadcast-node
- POST /add_transaction/broadcast
