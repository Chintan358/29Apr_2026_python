#map

# l = [10,20,30,40,50,60]
# # def square(a):
# #     return a*a
# k = map(lambda a:a*a,l)
# print(list(k))

# l = ["python","java","php","android"]
# # k = map(lambda a:len(a),l)
# # print(list(k))

# print(len(l[0]))

#filter
# l = [1,5,6,7,8,9,4,6,5,3,4]
# k = filter(lambda a:a%2!=0,l)
# print(list(k))


# l = ["python","java","php","android"]
# k = filter(lambda a:a.startswith("p"),l)
# print(list(k))

#reducer
# from functools import reduce
# l = [1,5,6,7,8,9,4,6,5,3,4]

# # k = reduce(lambda a,b:a+b,l)
# k = reduce(lambda a,b: a if a<b else b ,l)
# print(k)

# import math
# l = [1,5,6,7,8,9,6,5,3,4]

# k = filter(lambda a : math.sqrt(a).is_integer(),l)
# print(list(k))


# l = ["python","java","php","android"]
# k = filter(lambda a : "o" in a , l)
# print(list(k))


# l = [10,20,30,40,50,60,70,80]

# k = iter(l)
# print(next(k))
# print(next(k))

# print(next(k))


def square(a):
    for i in range(a):
        yield i*i
    
r = square(10)
print(next(r))
print(next(r))
print(next(r))
print(next(r))