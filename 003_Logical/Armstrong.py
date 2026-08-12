number = 163
temp = number
sum = 0
while number!=0:
    rem = number%10
    sum+=(rem*rem*rem)
    number = number//10

if temp==sum:
    print("armstrong")
else:
    print("not armstrong")