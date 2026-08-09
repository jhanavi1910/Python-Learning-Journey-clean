class bank:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amt):
        self.balance+=amt
    def display(self):
        print("current balance is:",self.balance)
balance=int(input('enter the balance: '))
amt=int(input("enter the amount to deposit:"))
acc=bank(balance)
acc.deposit(amt)
acc.display()

    
        