# f  = open("test.txt",'w')
# # f.write("Hello python")
# f.writelines(["python\n","jav\n","Php"])
# f.close()

# f = open("test.txt",'r')
# data  =f.read()
# print(data)

# f = open("test.txt",'a')
# f.write("Python")
# f.close()

# f = open("test.txt",'r')
# data  =f.read()
# data = f.readlines()

# while True : 
#     data = f.readline()
#     if data.startswith("P"):
#         print(data)
#     if not data:
#         break


# with open("test.txt",'r') as f:
#     f.seek(5)
#     print(f.tell())
#     data = f.read()
#     print(f.tell())
#     print(data)

# with open("home.txt",'a+') as f : 
#     f.write("write anything")
#     f.seek(0)
#     data = f.read()
#     print(data)


# with open("a.jpg",'rb') as f:
#     data = f.read()
#     print(data)

import json
# k = {"name":"abc","email":"abc@gmail.com"}

# with open("data.json",'w') as f:
#     json.dump(k,f)


with open("data.json",'r') as f:
    k = json.load(f)
    print(k)

