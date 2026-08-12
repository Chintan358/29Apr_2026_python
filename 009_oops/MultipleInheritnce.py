class A : 
    
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
    def display(self):
        print(self.name,self.email)
        

class B : 
    
    def __init__(self,name,email,phone):
        self.name =name
        self.email = email
        self.phone = phone
        
    def display(self):
        print(self.name,self.email,self.phone)
        
        
class C(A,B):
    
    def __init__(self, name, email):
        super().__init__(name, email)



c  = C("test","test@gmail.com")
c.display()
    
        