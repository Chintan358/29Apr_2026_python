# s = {10,20,30,40,50,30,0,False,True,1}
# print(s)

# if 100 in s:
#     print(100)

# for i in s:
#     print(i)

# k = {10,20,30,40,50}
# k.add(500)
# k.remove(100)
# k.discard(100)
# print(k)


a = {10,20,30,40,50}
b = {40,50,60,70,80}

# a.update(b)
# k = a.union(b)
# k = a | b
# print(k)

# a.intersection_update(b)
# k = a.intersection(b)
# k = a&b
# print(k)

# a.difference_update(b)
# k = a.difference(b)
# k = b-a
# print(k)

# a.symmetric_difference_update(b)
# k = a.symmetric_difference(b)
k = a^b
# print(k)

# f = frozenset({10,20,30,40,50})
# print(f)

# i = {10,20}
# j = {10,20,30,40}
# print(i.issubset(j))
# print(j.issuperset(i))
# print(i.isdisjoint(j))