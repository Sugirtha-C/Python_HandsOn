class BankAccount:

    def __init__(self,account_number, account_holder,balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        print("Deposited amount:", amount)
        print("Balance after deposit:")
        self.balance+= amount
        print(self.balance)

    def withdraw(self,amount):
        print("withdrawal amount:",amount)
        print("Balance after withdrawal:")
        self.balance-=amount
        print (self.balance)

    def display_info(self):
        print("Account Number",self.account_number, "Account holder",self.account_holder,"Balance:",self.balance)




