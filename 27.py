from functions import simpleseive
from time import clock as now
primes = simpleseive(10000)
primes2 = simpleseive(1000)

def f(a,b,x):
    return x**2 + a*x + b

def brute():
    m = (0,0,0)
    for a in range(1000):
        #print(a)
        for b in primes2:
            for x in range(200):
                if f(a,b,x) not in primes:
                    if x > m[2]:
                        m = (a,b,x)
                        #print(m)
                    break
            for x in range(200):
                if f(-a,b,x) not in primes:
                    if x > m[2]:
                        m = (-a,b,x)
                        #print(m)
                    break
    print(m)
    print(now())

brute()
