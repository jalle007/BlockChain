from blockchain import Blockchain

def main():
    # Initialize the blockchain
    my_blockchain = Blockchain()

    # Add new blocks
    my_blockchain.add_block("First Block Data")
    my_blockchain.add_block("Second Block Data")

    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    # Validate the blockchain
    print("Is blockchain valid?", my_blockchain.is_chain_valid())

    # To test invalid data, try tampering with the chain:
    my_blockchain.chain[1].data = "Tampered Data"
    print("Is blockchain valid after tampering?", my_blockchain.is_chain_valid())

if __name__ == "__main__":
    main()
