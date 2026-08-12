# class Test:
    
#     def __init__(self):
#         print("inint calling")
        
#     def __str__(self):
#         return "manish"
        
# t = Test()   
# print(t)


# class Calc:
    
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
        
#     def __eq__(self, value):
#         return self.a==value.a and self.b==value.b
        
#     def __add__(self, other):
#         return self.a+other.a,self.b+other.b
    
#     def __mul__(self, other):
#         return self.a*other.a,self.b*other.b

# c1 = Calc(10,20)
# c2 = Calc(10,20)

# print(c1==c2)   
# print(c1+c2) 
# print(c1*c2)


class Demo:
    
    def __init__(self,a):
        self.a = a
        
    def __len__(self):
        return len(self.a)
        
    def __getitem__(self, key):
        return self.a[key]
    
    def __setitem__(self, key, value):
        self.a[key] = value
        
d = Demo([10,20,30,40,50,60])
# print(len(d))
# print(d[1])
d[1] = 500
print(d.a)