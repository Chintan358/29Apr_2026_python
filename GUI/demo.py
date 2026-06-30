from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("My App")

# b1 = Button(root,text="left").pack(side=LEFT)
# b2 = Button(root,text="right").pack(side=RIGHT)
# b3 = Button(root,text="top").pack(side=TOP)
# b4 = Button(root,text="bottom").pack(side=BOTTOM)


# l1= Label(root,text="Username")
# l1.grid(row=1,column=1)

# l2= Label(root,text="Email")
# l2.grid(row=2,column=1)

# l3= Label(root,text="Phone")
# l3.grid(row=3,column=1)

# e1 = Entry(root)
# e1.grid(row=1,column=2)
# e2 = Entry(root)
# e2.grid(row=2,column=2)
# e3 = Entry(root)
# e3.grid(row=3,column=2)

# b1  =Button(root,text="Submit")
# b1.grid(row=4,column=2)




l1= Label(root,text="Username")
l1.place(x=100,y=100)

l2= Label(root,text="Email")
l2.place(x=100,y=150)

l3= Label(root,text="Phone")
l3.place(x=100,y=200)

e1 = Entry(root)
e1.place(x=200,y=100)
e2 = Entry(root)
e2.place(x=200,y=150)
e3 = Entry(root)
e3.place(x=200,y=200)

b1  =Button(root,text="Submit",width=15)
b1.place(x=200,y=230)

root.mainloop()