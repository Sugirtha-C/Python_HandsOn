from basics.bankAccManagement.BankAccount import BankAccount


class CheckingAccount(BankAccount):

    def __init__(self,account_number,account_holder,balance,overdraft_limit):

        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
        self.overdraft_limit=overdraft_limit

    def withdraw(self,amount):

        print("Method overridden to allow overdraft withdrawals")
        print("withdrawal amount:", amount)
        print("Balance after withdrawal:")
        self.balance -= amount
        print(self.balance)

    def display_info(self):

        print("Acc Number",self.account_number,"Acc Holder:", self.account_holder,"Balance:",self.balance,"overdraft_limit",self.overdraft_limit)

print("==============================================================================")
print("Displaying details from child class: CheckingAccount")
checkAcc=CheckingAccount(100520,"John Mathew",500000.52,5000)
checkAcc.display_info()
checkAcc.withdraw(20950)
checkAcc.display_info()
print("==============================================================================")

print("==============================================================================")
print("Displaying details from main class Bank Account")
bankAcc=BankAccount(100520,"John Snow",485500.52)
print("Initial balance:")
bankAcc.display_info()
print("Balance after deposit")
bankAcc.deposit(95000)
print("Balance after withdrawal:")
bankAcc.withdraw(600)
print("Displaying details:")
bankAcc.display_info()
print("==============================================================================")


