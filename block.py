import hashlib
import time

class Block:
    # Constructor for the Block class.
    # Initializes a block with index, data, previous hash, and computes its hash.
    def __init__(self, index, previous_hash, data, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce  # Used for Proof of Work
        self.hash = self.calculate_hash()

    # Generates the hash for the block using SHA-256.
    # Includes index, timestamp, data, previous hash, and nonce in the hash computation.
    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    # Performs the Proof of Work by finding a hash with a specified number of leading zeros.
    # Parameters:
    # - difficulty: Number of leading zeros required in the hash.
    def mine_block(self, difficulty):
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()
