# class Sample:
    
#     def __init__(self):
#         print("init calling")
    
#     def display(self):
#         print("display calling")
        
# s = Sample()
# s.display()


class Student:
    
    #class attribute
    clg = 'ABC'
    
    
    def __init__(self,name,email,age):
        #instance attribute
        self.name = name
        self.email = email
        self.age = age
        
    def display(self):
        print(self.name,self.email,self.age,self.clg)
        
    @classmethod
    def run(cls):
        print(cls.clg)
        
    @staticmethod
    def show():
        print("show calling")
        
Student.clg = "XYZ"
s = Student("saed","saed@gmail.com",22)
s.display()
s1 = Student("Priya","priya@gmail.com",22)
s1.display()
Student.run()
Student.show()