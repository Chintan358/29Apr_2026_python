# def test():
#     print("test calling")

# def square(a):
#     print(a*a)


# def add(a,b):
#     print(a+b)

# def message():
#     return "Hello"

# def cube(a):
#     return a*a*a

# test()
# square(10)
# square(20)
# add(10,20)
# t = message()
# print(t)
# print(message())
# print(cube(3))


# def person(name,email,age):
#     print(name,email,age)

# person("abc","abc@gmail.com",25)

# def person(name,email="xyz@gmial.com",age=25):
#     print(name,email,age)

# person("abc",age=25)


# def sum(*a):
#     sum =0
#     for i in a:
#         sum+=i
#     print(sum)

# sum(10,20,30,50)

    # def student(**a):
    #     print(a)

    # student(name="saed",email="saed@gmail.com",age=23)





add = lambda a,b:a+b
sq = lambda a:a*a

print(add(10,20))
print(sq(10))