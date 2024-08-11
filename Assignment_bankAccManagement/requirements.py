
"""
Bank Account Management System
Scenario:
You are tasked with creating a bank account management system that includes different types of bank accounts. Each account has common attributes and behaviors, but also specific attributes and behaviors depending on the type of account. You need to implement a base class BankAccount and two derived classes SavingsAccount and CheckingAccount.
Requirements:
Base Class BankAccount:
Attributes:
account_number (str): The account number.
account_holder (str): The name of the account holder.
balance (float): The balance of the account.
Methods:
__init__(self, account_number, account_holder, balance): Constructor to initialize the attributes.
deposit(self, amount): Method to deposit an amount into the account.
withdraw(self, amount): Method to withdraw an amount from the account.
display_info(self): A method to display the account's information.
Derived Class SavingsAccount (inherits from BankAccount):
Additional Attribute:
interest_rate (float): The interest rate of the savings account.
Methods:
__init__(self, account_number, account_holder, balance, interest_rate): Constructor to initialize all attributes.
add_interest(self): Method to add interest to the balance based on the interest rate.
display_info(self): Override this method to display savings account-specific information.
Derived Class CheckingAccount (inherits from BankAccount):
Additional Attribute:
overdraft_limit (float): The overdraft limit for the checking account.
Methods:
__init__(self, account_number, account_holder, balance, overdraft_limit): Constructor to initialize all attributes.
withdraw(self, amount): Override this method to allow overdraft withdrawals.
display_info(self): Override this method to display checking account-specific information.

"""