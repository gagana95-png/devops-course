
Hi Ankit,


class BankAccount:
    def __init__(self):
        self.balance = 0
        
    def withdraw(self, amount):
       self.balance =  self.balance - amount 
       return
    def deposit(self, amount):
       self.balance =  self.balance + amount
       return
    def bal_check(self):
       print(self.balance)
       return

a = BankAccount()

a.deposit(100)
a.withdraw(40)
a.bal_check()

class MinimumBalanceAccount(BankAccount):
   def __init__(self, name):
      self.minimum_balance=5000
      BankAccount.__init__(self)
    
      
      
   def withdraw(self, amount):
      if self.balance - amount < 5000:
          print('Sorry, minimum balance must be maintained.')
      else:
          BankAccount.withdraw(self, amount)
          
          
b = MinimumBalanceAccount("gagana")
b.withdraw(50)

