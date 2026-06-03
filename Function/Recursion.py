
def test(a):
    print(a*a)
    a+=1
    if a<20:
        test(a)

test(1)