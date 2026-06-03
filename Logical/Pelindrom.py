# number = 123454321
# temp = number
# sum = 0
# while number!=0:
#     rem = number%10
#     sum = (sum*10)+rem
#     number//=10

# if temp==sum:
#     print("Pelindrom")
# else:
#     print("Not pelindrom")


st = "abcba"
rev = st[::-1]
if st==rev:
    print("pelindrom")
else:
    print("Not pilindrom")
