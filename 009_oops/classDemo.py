class Pen:
    price = 100
    color = "red"
    company = "cello"
    
    def to_write(self):
        print(self.price,self.color,self.company)

p1 = Pen()
p1.color="black"
p1.to_write()

p2 = Pen()
p2.to_write()