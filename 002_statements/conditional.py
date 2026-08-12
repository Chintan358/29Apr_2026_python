#conditional : if-else , match-case
#looping : for, while
#control : break,continue, pass

a = 100
b = 200
c = 300

# if a>b:
#     if a>c:
#         print("A is greater")
#     else:
#         print("C is greater")
# else:
#     if b>c:
#         print("B is greater")
#     else:
#         print("C is greater")


# if a>b and a>c:
#     print("A is greater")
# elif b>a and b>c:
#     print("B is grater")
# elif c>a and c>b:
#     print("C is greater")
# else:
#     print("something went wrong")


# marks = 45
# 91-100 : a
# 71-90 - b
# 51-70:c
# 35 - 50 : d 
# 0 - 34 - F



choice = 34
match(choice):
    case 1 : print("Gujarati")
    case 2 : print("Hindi")
    case 3 : print("english")
    case _: print("invalid choice")