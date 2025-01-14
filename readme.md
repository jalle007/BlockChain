# Blockchain Tutorial App

## Introduction to Blockchain

Blockchain is a decentralized, distributed ledger technology that records transactions across many computers so that the record cannot be altered retroactively without the alteration of all subsequent blocks and the consensus of the network. It is the underlying technology behind cryptocurrencies like Bitcoin and Ethereum.

### Key Concepts

- **Block**: A block is a container data structure that stores transactions.
- **Chain**: A chain is a sequence of blocks, each linked to the previous one.
- **Decentralization**: Blockchain operates on a peer-to-peer network without a central authority.
- **Consensus Mechanism**: A process used to achieve agreement on a single data value among distributed processes or systems.

## Running the App

This tutorial app demonstrates basic blockchain concepts, smart contracts, and peer-to-peer (P2P) networking.

### Prerequisites

- Python 3.x
- Required Python packages (install using `pip`):
    ```bash
    pip install -r requirements.txt
    ```

### Basic Blockchain Example

To run the basic blockchain example, execute the following command:

```bash
python app.py
```

This will create a simple blockchain and add a few blocks to it. The blockchain will be printed to the console.

### Smart Contract Example

The smart contract example demonstrates how to create and execute a simple smart contract. The contract rewards a user after 5 blocks are mined.

To run the smart contract example, execute the following command:

```bash
python app.py
```

The output will show the execution of the reward action after the 5th block is added.

### P2P Example

The P2P example demonstrates how to set up a peer-to-peer network and broadcast the blockchain to connected peers.

To run the P2P example, uncomment the `p2p_example` function call in the `main` function of `app.py` and execute the following command:

```bash
python app.py [port] [peer_host] [peer_port]
```

- `port`: The port number to start the P2P server (default is 5000).
- `peer_host`: The hostname of the peer to connect to (optional).
- `peer_port`: The port number of the peer to connect to (optional).

Example:

```bash
python app.py 5001 localhost 5000
```

This will start the P2P server on port 5001 and connect to a peer running on `localhost` at port 5000.

## Conclusion

This tutorial app provides a basic understanding of blockchain technology, smart contracts, and P2P networking. Feel free to explore and modify the code to deepen your understanding of these concepts.
