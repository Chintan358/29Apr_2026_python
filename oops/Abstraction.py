from abc import ABC,abstractmethod

class Account(ABC):
    balance = 0
    
    @abstractmethod
    def deposite(self,amount):
        pass
    
    @abstractmethod
    def withdrow(self,amount):
        pass
    
    def get_balance(self):
        print(f"current balance is {self.balance}")
    
class Saving(Account):

    def deposite(self, amount):
        self.balance+=amount
        
    def withdrow(self, amount):
        if amount>self.balance:
            print("Insufficent amount")
        else:
            self.balance-=amount
            
class Loan(Account)  :
    def deposite(self, amount):
        if amount >=self.balance:
            t = amount-self.balance
            self.balance=0
            print(f"you have left more {t}")
        else:
            self.balance-=amount
            
    
    def withdrow(self, amount):
        self.balance+=amount        
            
            
# s = Saving()
# s.get_balance()
# s.deposite(5000)
# s.deposite(2000)
# s.withdrow(5000)
# s.get_balance()

l = Loan()
l.get_balance()
l.withdrow(5000)
l.deposite(3000)
l.get_balance()