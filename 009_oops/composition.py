class Salary:
    
    def __init__(self,salary,bonus):
        self.salary = salary
        self.bonus = bonus
        
    def annual_salary(self):
        return (self.salary*12)+self.bonus
    
    
class Emp:
    
    def __init__(self,name,age,salary,bonus):
        self.name=  name
        self.age = age
        self.s  = Salary(salary,bonus)
      
    def total_sal(self):
        print(f"total salary of {self.name} is {self.s.annual_salary()}")  
    
    
        
e = Emp("Vivek",25,5000,1000)
e.total_sal()