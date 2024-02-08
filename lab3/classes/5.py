class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, plus):
        self.balance += plus
        
    def withdraw(self, minus):
        if minus > self.balance:
            print ("You cannot withdraw money, your balance is not enough to withdraw")
        else:
            self.balance -= minus
    
    def info(self):
        print ("Hello", self.owner, "your balance is", self.balance)
        
a = BankAccount(input("Your name: "), int(input("Your balance: ")))
a.deposit(int(input("How much money do you want to deposit: ")))
a.withdraw(int(input("How much money do you want to withdraw: ")))
a.info()
