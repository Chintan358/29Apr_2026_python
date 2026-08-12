class Salary:
    
    def __init__(self,salary,bonus):
        self.salary = salary
        self.bonus = bonus
        
    def annual_salary(self):
        return (self.salary*12)+self.bonus
    
    
class Emp:
    
    def __init__(self,name,age,s):
        self.name=  name
        self.age = age
        self.s  = s
      
    def total_sal(self):
        print(f"total salary of {self.name} is {self.s.annual_salary()}")  
       
        
s = Salary(5000,1000)
e = Emp("Vivek",25,s)
e.total_sal()