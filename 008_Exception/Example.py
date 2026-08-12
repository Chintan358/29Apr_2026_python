try : 
    # a = 10/0
    # print(a)
    print("a"+10)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)