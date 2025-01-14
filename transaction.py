class Transaction:
    # Constructor for the Transaction class.
    # Initializes a transaction with sender, recipient, and amount.
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    # Returns a string representation of the transaction for easy viewing.
    def __repr__(self):
        return f"Transaction({self.sender} -> {self.recipient}, Amount: {self.amount})"
