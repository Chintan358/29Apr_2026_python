# l = [1,2,3,4,5,6,7,8,9]
# r = []
# def checkodd(n):
#     if n%2!=0:
#         return n
    
# for i in l:
#     k = checkodd(i)
#     if k is not None:
#         r.append(k)

# r = filter(checkodd,l)
# r = filter(lambda a : a%2!=0,l)
# print(list(r))

# subjects = ["java","python","android","node","react","php"]

# k = filter(lambda k : "a" in k,subjects)
# k = filter(lambda k : k.startswith("p"),subjects)
# print(list(k))

import math

l = [1,2,3,4,5,6,7,8,9]


k = filter(lambda a : math.sqrt(a).is_integer(),l)
print(list(k))