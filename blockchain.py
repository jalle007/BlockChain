from block import Block

class Blockchain:
    # Constructor for the Blockchain class.
    # Initializes the blockchain with the genesis block.
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Set the mining difficulty level.

    # Creates the first block in the blockchain, called the Genesis Block.
    # Returns a Block object with index 0 and arbitrary previous hash/data.
    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    # Retrieves the most recent block in the chain.
    # Returns the last block in the blockchain.
    def get_latest_block(self):
        return self.chain[-1]

    # Adds a new block to the blockchain after mining it.
    # Parameters:
    # - new_data: The data to be stored in the new block.
    def add_block(self, new_data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), latest_block.hash, new_data)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    # Validates the entire blockchain.
    # Ensures each block's hash is correct and matches the previous block's hash.
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate current block's hash
            if current_block.hash != current_block.calculate_hash():
                print(f"Block {current_block.index} has invalid hash!")
                return False

            # Validate hash linking with previous block
            if current_block.previous_hash != previous_block.hash:
                print(f"Block {current_block.index} is not linked correctly to the previous block!")
                return False

        # print("Blockchain is valid.")
        return True
