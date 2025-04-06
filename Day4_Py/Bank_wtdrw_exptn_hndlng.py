class InsufficientFundsError(Exception):
    """Custom exception for insufficient balance"""
    def __init__(self, balance, amount):
        super().__init__(f"Attempted to withdraw ₹{amount}, but only ₹{balance} available.")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        
        :param amount: Amount to withdraw
        :return: Remaining balance or error message
        """
        try:
            # TODO: Implement withdrawal logic
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
            if self.balance>=amount :
                self.balance = self.balance-amount
                return self.balance
            else:
                raise InsufficientFundsError(self.balance,amount)
            pass  
        except ValueError as e:
            return f"you have entered {amount} that is value error : {e}"
        # TODO: Handle negative withdrawal amounts
        except InsufficientFundsError as e:
            return f"Insufficient balance : {e}"
        # TODO: Handle insufficient funds
        except Exception as e:
            pass  # TODO: Handle unexpected errors

# Example Usage:
account = BankAccount(100)
print(account.withdraw(150))  # Should raise InsufficientFundsError
print(account.withdraw(-10))  # Should raise ValueError
