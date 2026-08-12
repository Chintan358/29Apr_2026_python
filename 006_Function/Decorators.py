
# def before(func):
#     def execute():
#         print("calling before test")
#         func()
#     return execute

# def after(func):
#     def execute():  
#         func()
#         print("calling after test")
#     return execute


# @after
# @before
# def test():
#     print("test calling")
    
# test()


# def add(func):
#     def exceute(*a):
#         sum =0
#         for i in a:
#             sum +=i
#         print(f"addtion is {sum}")
#         func(*a)
#     return exceute

# def mul(func):
#     def exceute(*a):
#         sum =1
#         for i in a:
#             sum *=i
#         print(f"multiplication is {sum}")
#         func(*a)
#     return exceute

# @mul
# @add
# def calc(a,b):
#     pass

# calc(10,20)


def numbers_only(func):
    def execute(a):
        if str(a).isdigit():
            func(a)
        else:
            print("Invalid input")
    return execute

def chars_only(func):
    def execute(a):
        if str(a).isalpha():
            func(a)
        else:
            print("Invalid input")
    return execute

@chars_only
def get(a):
    print(a)
    
get("fdf")




