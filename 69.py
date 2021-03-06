from functions import simpleseive as seive

primes = seive(1000,2)
#print(primes)


def phi(n):
    t = 1
    n1 = n*1
    for p in primes:
        c = 0
        while n1 % p == 0:
            n1 = n1/p
            c += 1
        if c > 0:
            t *= (p-1)*p**(c-1)
            #print(n1,p,c)
    if n1 != 1:
        t *= n1-1
    return t

nmax = 0
m = 0
for n in range(1,1000001):
    trial = float(n)/phi(n)
    if trial > m:
        nmax = n
        m = trial
        print(nmax,m)


    

