# parent - super - base
class A:
    a = 10
    
    def display(self):
        print(self.a)
        
# child - sub - derived       
class B(A):
    
    a = 50
    def show(self):
        print("show calling")
        print(self.a)
        print(super().a)
        
# class C(B):
#     pass      
        
# class C(A):
#     pass

# class C(A,B):
#     pass
    
        
b = B()
b.show()
# b.display()