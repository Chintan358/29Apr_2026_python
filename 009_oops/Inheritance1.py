class Pen:
    
    def __init__(self,price, color, company):
        self.price = price
        self.color = color
        self.company = company
        
    def display(self):
        print(self.color,self.company,self.price)
        
        
class Notebook(Pen):
    
    def __init__(self, price, color, company,pages):
        super().__init__(price, color, company)
        self.pages = pages
        
    def display(self):
        print(self.color,self.price,self.company,self.pages)
    
        
p = Pen(100,"RED","Cello")
p.display()

n = Notebook(150,"White","Classmate",500)
n.display()