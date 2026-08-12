print("Program started")

try:
    a = 10
    b = a/0
    print(b)
except Exception as e:
    print(e)
else:
    print("code run successfully")
finally:
    print("always exceutable block")


print("program ended")