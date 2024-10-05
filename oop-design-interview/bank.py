from abc import ABC, abstractmethod
from typing import List

class Transaction(ABC):
    def __init__(self, customerId: int, tellerId: int):
        self._customerId = customerId
        self._tellerId = tellerId

    def get_customer_id(self):
        return self._customerId
    
    def get_teller_id(self):
        return self._tellerId
    
    @abstractmethod
    def get_transaction_description(self):
        pass
    

class Deposit(Transaction):
    def __init__(self, customerId: int, tellerId: int, amount: float):
        super().__init__(customerId, tellerId)
        self._amount = amount

    def get_transaction_description(self):
        return f'Teller {self.get_teller_id()} deposited {self._amount} to account {self.get_customer_id()}'
    
class Widthdraw(Transaction):
    def __init__(self, customerId: int, tellerId: int, amount: float):
        super().__init__(customerId, tellerId)
        self._amount = amount

    def get_transaction_description(self):
        return f'Teller {self.get_teller_id()} withdrew {self._amount} from account {self.get_customer_id()}'
    
class OpenAccount(Transaction):
    def __init__(self, customerId: int, tellerId: int):
        super().__init__(customerId, tellerId)

    def get_transaction_description(self):
        return f'Teller {self.get_teller_id()} opened account {self.get_customer_id()}'
    
class BankTeller:
    def __init__(self, id: int):
        self._id = id

    def get_id(self):
        return self._id
    

import random

class BankBranch:
    def __init__(self, address: str, cash_on_hand: float, bank_system: 'BankSystem'):
        self._address = address
        self._cash_on_hand = cash_on_hand
        self._bank_system = bank_system
        self._tellers = []


    def add_teller(self, teller):
        self._tellers.append(teller)

    def _get_available_teller(self):
        index = round(random.random() * (len(self._tellers) - 1))
        return self._tellers[index].get_id()
    
    def open_account(self, customer_name):
        if not self._tellers:
            raise ValueError('Branch does not have any tellers')
        
        teller_id = self._get_available_teller()
        return self._bank_system.open_account(customer_name, teller_id)
    
    def deposit(self, customer_id, amount):
        if not self._tellers:
            raise ValueError('Branch does not have any tellers')
        
        teller_id = self._get_available_teller()
        self._bank_system.deposit(customer_id, teller_id, amount)

    def withdraw(self, customer_id, amount):
        if amount > self._cash_on_hand:
            raise ValueError('Branch does not have enough cash')
        if not self._tellers:
            raise ValueError('Branch does not have any tellers')
        
        self._cash_on_hand -= amount
        teller_id = self._get_available_teller()
        self._bank_system.withdraw(customer_id, teller_id, amount)

    def collect_cash(self, ratio):
        cash_to_collect = round(self._cash_on_hand * ratio)
        self._cash_on_hand -= cash_to_collect
        return cash_to_collect
    
    def provide_cash(self, amount):
        self._cash_on_hand += amount

class BankAccount:
    def __init__(self, customer_id: int, name: str, balance: float):
        self._customer_id = customer_id
        self._name = name
        self._balance = balance

    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount
        
class BankSystem:
    def __init__(self, accounts: List[BankAccount], transactions: List[Transaction]):
        self._accounts = accounts
        self._transactions = transactions

    def get_account(self, customerId):
        return self._accounts[customerId]
    
    def get_accounts(self):
        return self._accounts
    
    def get_transactions(self):
        return self._transactions
    
    def open_account(self, customer_name, teller_id):
        # Create a new account
        customerId = len(self.get_accounts())
        account = BankAccount(customerId, customer_name, 0)
        self._accounts.append(account) # could be also a dictionary with customerId as key

        # Log transaction
        transaction = OpenAccount(customerId, teller_id)
        self._transactions.append(transaction)

        return customerId
    

    def deposit(self, customerId, teller_id, amount):
        account = self.get_account(customerId)
        account.deposit(amount)

        transaction = Deposit(customerId, teller_id, amount)
        self._transactions.append(transaction)


    def withdraw(self, customerId, teller_id, amount):
        if amount > self.get_account(customerId).get_balance():
            raise ValueError('Not enough balance')
        
        account = self.get_account(customerId)
        account.withdraw(amount)

        transaction = Widthdraw(customerId, teller_id, amount)
        self._transactions.append(transaction)

class Bank:
    def __init__(self, branches: List[BankBranch], bank_system: BankSystem, total_cash: float = 0):
        self._branches = branches
        self._bank_system = bank_system
        self._total_cash = total_cash

    def add_branch(self, address, initial_fund):
        branch = BankBranch(address, initial_fund, self._bank_system)
        self._branches.append(branch)
        return branch

    def collect_cash(self, ratio):
        for branch in self._branches:
            cash_collected = branch.collect_cash(ratio)
            self._total_cash += cash_collected

    def print_transactions(self):
        for transaction in self._bank_system.get_transactions():
            print(transaction.get_transaction_description())

        print('End of transactions')

if __name__ == '__main__':
    bankSystem = BankSystem([], [])
    bank = Bank([], bankSystem, 10000)

    branch1 = bank.add_branch('123 Main St', 1000)
    branch2 = bank.add_branch('456 Elm St', 1000)

    branch1.add_teller(BankTeller(1))
    branch1.add_teller(BankTeller(2))
    branch2.add_teller(BankTeller(3))
    branch2.add_teller(BankTeller(4)) 

    customerId1 = branch1.open_account('John Doe')
    customerId2 = branch1.open_account('Bob Smith')
    customerId3 = branch2.open_account('Jane Doe')

    branch1.deposit(customerId1, 100)
    branch1.deposit(customerId2, 200)
    branch2.deposit(customerId3, 300)

    branch1.withdraw(customerId1, 50)


    bank.print_transactions()

          