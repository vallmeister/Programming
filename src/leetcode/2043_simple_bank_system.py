from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.bank_accounts = balance

    def is_valid(self, account, money):
        n = len(self.bank_accounts)
        return 1 <= account <= n and self.bank_accounts[account - 1] >= money

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.is_valid(account1, money) or not self.is_valid(account2, 0):
            return False
        self.bank_accounts[account1 - 1] -= money
        self.bank_accounts[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.is_valid(account, 0):
            return False
        self.bank_accounts[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_valid(account, money):
            return False
        self.bank_accounts[account - 1] -= money
        return True


bank = Bank([10, 100, 20, 50, 30])
print(bank.withdraw(3, 10))
print(bank.transfer(5, 1, 20))
print(bank.deposit(5, 20))
print(bank.transfer(3, 4, 15))
print(bank.withdraw(10, 50))
