from time import clock as now

def test(n):
    l = []
    e = 1
    while n**e < 101:
        e += 1

    for i in range(1,e):
        for j in range(2,101):
            x = (2**i)**j
            if x not in l:
                l.append(x)
    return(len(l))


def pb29():
    ans = 0
    nums = [True]*99
    for i in range(2,101):
        if nums[i-2]:
            e = 1
            while i**e < 101:
                #print(i**e)
                nums[i**e-2] = False
                e += 1
            ans += test(i)
            print(i,test(i))
    print( ans)

def brute():
    l = []
    for a in range(2,101):
        for b in range (2,101):
            c = a**b
            if c not in l:
                l.append(c)
    print len(l)

pb29()
print(now())
brute()
print(now())


