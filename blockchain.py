from block import Block
from transaction import Transaction
from smart_contract import SmartContract

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.pending_transactions = []
        self.smart_contracts = []  # List of registered smart contracts.

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def add_block(self, miner_reward):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), latest_block.hash, str(self.pending_transactions))
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = [Transaction("System", "Miner", miner_reward)]

    # Registers a smart contract to be executed on the blockchain.
    def register_smart_contract(self, contract):
        self.smart_contracts.append(contract)

    # Executes all registered smart contracts if their conditions are met.
    def execute_smart_contracts(self):
        for contract in self.smart_contracts:
            executed = contract.execute(self)
            if executed:
                print(f"Smart Contract {contract.contract_id} executed.")


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
