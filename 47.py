from functions import simpleseive
from time import clock as now

def pb47():
    n = 0
    n1 = []
    n2 = []
    n3 = []
    print(now())
    primes = simpleseive(200000)
    print(now())
    while n < 200000:
        m = n
        n4 = []
        for p in primes:
            #print(m,p)
            if p > m:
                break
            if m % p == 0:
                while m % p == 0:
                    m = m / p
                    #print(m,p)
                n4.append(p)
                if len(n4) == 5:
                    break
        if len(n4) == len(n3) == len(n2) == len(n1)== 4:
            print(n-3,n-2,n-1,n,n*(n-1)*(n-2)*(n-3))
            return
        #print(n1,n2,n3,n4)
        n1,n2,n3 = n2 + [],n3 + [],n4 + []
        n += 1
    print(now())
pb47()
