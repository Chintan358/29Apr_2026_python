# student = {
#     "name":"mithilesh",
#     "email":"mithilesh@gmail.com",
#     "age":20
#     }


# print(student['name'])
# print(student.get("name1"))

# print(student.keys())
# print(student.values())
# print(student.items())

# print(student['name'])
# student['name1']="xyz"
# print(student)

# st = {"phone":"968748585","gender":"male"}
# student.update({"phone":"9685748596"})
# student.update(st)

# student.pop("name")
# student.popitem()
# student.clear()
# del student['name']
# del student
# print(student)



country = {
    "India":"IN",
    "USA":"US",
    "CANADA":"CAN"
}

# for i,j in country.items():
#     print(i,j)

# for i in country.keys():
#     print(i)

# k  = country.copy()
# k = dict(country)
# print(k)


# user = {
#     "name":"Priya",
#     "email":"priya@gmail.com",
#     "address": {
#         "country":"India",
#         "state":"gujarat",
#         "city":"surat"
#     }
# }

# print(user['address']['country'])

# x = ('key1', 'key2', 'key3')
# y = 0

# thisdict = dict.fromkeys(x, y)

# print(thisdict)

# a = ("k1","k2","k3")
# b = ("v1","v2","v3")

# k = zip(a,b)
# print(dict(k))
# print(list(k))



user = {
    "name":"Priya",
    "email":"priya@gmail.com",
}

# user['name'] = 25
user.setdefault("name",25)

print(user)