from basics.bankAccManagement.BankAccount import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self, account_number, account_holder, balance, interest_rate):

        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
        self.interest_rate=interest_rate

    def add_interest(self):

        print("Interest rates added to balance:",self.interest_rate)
        interest_perc=self.balance*(self.interest_rate/100)
        self.balance+=interest_perc
        print("Updated balance with interest rate:",self.balance)

    def display_info(self):

        print("Acc number:", self.account_number,"Acc holder:",self.account_holder,"Balance:",self.balance,"Interest Rate:", self.interest_rate )

print("==============================================================================")
print("Displaying details from main class Bank Account")
bankAcc=BankAccount(100520,"John Snow",45000.05)
print("Initial balance:")
bankAcc.display_info()
print("Balance after deposit")
bankAcc.deposit(40000)
print("Balance after withdrawal:")
bankAcc.withdraw(500)
print("Displaying details:")
bankAcc.display_info()
print("==============================================================================")
print("==============================================================================")
print("Displaying details from child class Savings account:")
savingsAcc=SavingsAccount(10400,"Denarys",60000,5.5)
print("Details before adding interest to balance:")
savingsAcc.display_info()
print("Details after adding interest to balance:")
savingsAcc.add_interest()
savingsAcc.display_info()
print("==============================================================================")