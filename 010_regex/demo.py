import re

# st = "sun rises in rks in"

# k = re.match("s", st )
# k = re.search("in", st)
# k = re.findall("in", st)
# k = re.finditer("in", st)
# print(next(k).span())
# print(next(k).span())

# k = re.sub("in", "on", st)
# print(k)

# k = re.split("i", st)
# print(k)



# k = re.findall("s.n", "sun risn in rks in")
# k = re.findall("^in", "sun risn in rks in")
# k = re.findall("in$", "sun risn in rks in")
# k = re.findall("sa*n", "sun risn in rks in")
# k = re.findall("su+n", "sun risn in rks in")
# k = re.findall("su?n", "sn risn in rks in")
# print(k)


# k = re.findall(r"\bsun", "sun sunrisunsn in rks in 5 6 58 @")
# print(k)



# k = re.search(r"^[0-9]{10}$", "1234567890")
# if k is not None:
#     print("valid")
# else:
#     print("invalid")


# pattern = r"^[0-9a-zA-Z._-]+@[a-zA-Z]+\.[a-zA-Z]{2,4}+$"
# k = re.search(pattern, "tops@gmail.com")
# if k is not None:
#     print("valid")  
# else:
#     print("invalid")

k = re.search(r"[a-zA-Z]{2,10}", "priya")
print(k)