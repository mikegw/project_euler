from functions import simpleseive as seive

primes = seive(4000,2)
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

def digits_of(n):
    r = [int(d) for d in str(n)]
    r.sort()
    return r

nmin = 0
m = 5
for i in range(80,100):
    print(i)
    for n in range(i*100000,(i+1)*100000):
        for p in [2,3,5,7,11,13,17,23,29]:
            if n % p == 0:
                break
        else:
            t = phi(n)
            dt = digits_of(t)
            dn = digits_of(n)
            if dt == dn:
                trial = float(n)/t
                if trial < m:
                    nmin = n
                    m = trial
                    print(n, phi(n),m)
