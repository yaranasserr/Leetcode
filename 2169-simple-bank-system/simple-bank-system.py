from typing import List

class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)  # Store the number of accounts

    def is_valid_account(self, account: int) -> bool:
        return 1 <= account <= self.n  # Check if the account is within valid range

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.is_valid_account(account1) and self.is_valid_account(account2):
            account1 -= 1  # Adjust 1-based index to 0-based
            account2 -= 1
            if self.balance[account1] >= money:
                self.balance[account1] -= money
                self.balance[account2] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.is_valid_account(account):
            account -= 1  # Adjust to 0-based index
            self.balance[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.is_valid_account(account):
            account -= 1  # Adjust to 0-based index
            if self.balance[account] >= money:
                self.balance[account] -= money
                return True
        return False