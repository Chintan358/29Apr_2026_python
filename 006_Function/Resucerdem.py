from functools import reduce

l = [10,4,5,8,94,6,4,65]

# k = reduce(lambda a,b:a+b,l)
k = reduce(lambda a,b: a if a>b else b,l)
print(k)

