import sys
from p2p import P2PNode
from blockchain import Blockchain
from smart_contract import SmartContract

# Basic Blockchain Example
def basic_blockchain_example():
    # Create a new blockchain
    my_blockchain = Blockchain()

    # Add some blocks
    my_blockchain.add_block("First Block Data")
    my_blockchain.add_block("Second Block Data")

    # Print the blockchain
    for block in my_blockchain.chain:
        print(block)

# Smart Contract Example
def smart_contract_example():
    my_blockchain = Blockchain()

    # Example smart contract: Reward a user after 5 blocks are mined.
    def reward_condition(state):
        return len(state.chain) >= 5

    def reward_action():
        print("Reward action executed! User rewarded.")

    reward_contract = SmartContract(contract_id=1, conditions=reward_condition, action=reward_action)
    my_blockchain.register_smart_contract(reward_contract)

    # Add some blocks to trigger the contract.
    for i in range(5):
        my_blockchain.add_block("Block Data " + str(i))
        my_blockchain.execute_smart_contracts()

# P2P Example
def p2p_example():
    port = 5000  # Default port
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    my_blockchain = Blockchain()
    p2p_node = P2PNode(my_blockchain, port=port)
    p2p_node.start_server()

    # Connect to another peer if provided
    if len(sys.argv) > 3:
        peer_host = sys.argv[2]
        peer_port = int(sys.argv[3])
        p2p_node.connect_to_peer(peer_host, peer_port)

    # Add some blocks and broadcast
    my_blockchain.add_block("First Block Data")
    p2p_node.broadcast_chain()

def main():
    # Run basic blockchain example
    print("Running basic blockchain example...")
    basic_blockchain_example()

    # Run smart contract example
    print("\nRunning smart contract example...")
    smart_contract_example()

    # Uncomment the following line to run the P2P example
    # print("\nRunning P2P example...")
    # p2p_example()

if __name__ == "__main__":
    main()


# p2p example
# def main():
#     port = 5000  # Default port
#     if len(sys.argv) > 1:
#         port = int(sys.argv[1])

#     my_blockchain = Blockchain()
#     p2p_node = P2PNode(my_blockchain, port=port)
#     p2p_node.start_server()

#     # Connect to another peer if provided
#     if len(sys.argv) > 3:
#         peer_host = sys.argv[2]
#         peer_port = int(sys.argv[3])
#         p2p_node.connect_to_peer(peer_host, peer_port)

#     # Add some blocks and broadcast
#     my_blockchain.add_block("First Block Data")
#     p2p_node.broadcast_chain()

# if __name__ == "__main__":
#     main()

