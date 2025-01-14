class SmartContract:
    # Constructor for the SmartContract class.
    # Initializes a contract with a unique ID and a set of predefined conditions.
    #     Parameters:
    # - contract_id: Unique identifier for the contract.
    # - conditions: A function that evaluates whether the contract should execute.
    # - action: A function that defines what the contract does when conditions are met.
    def __init__(self, contract_id, conditions, action):
        self.contract_id = contract_id
        self.conditions = conditions
        self.action = action
        self.executed = False

    # Evaluates and executes the smart contract if conditions are met.
    def execute(self, blockchain_state):
        if not self.executed and self.conditions(blockchain_state):
            self.action()
            self.executed = True
            return True
        return False

    def __repr__(self):
        return f"SmartContract(ID: {self.contract_id}, Executed: {self.executed})"
