from functions import simpleseive as seive

primes = seive(10000,2)
#print('primed')

def digits_of(n):
    return set([d for d in str(n)])

m = 0
for i1 in range(1,len(primes)):
    for i2 in range(i1):
        p1 = primes[i1]
        p2 = primes[i2]
        if p1*p2 < 10000000:
            phi = (p1-1)*(p2-1) 
            if digits_of(phi) == digits_of(p1*p2):
                if p1*p2 > m:
                    m = p1*p2
                    print(m)

for i1 in range(2,len(primes)):
    for i2 in range(1,i1):
        for i3 in range(i2):
            p1 = primes[i1]
            p2 = primes[i2]
            p3 = primes[i3]
            if p1*p2*p3 < 10000000:
                phi = (p1-1)*(p2-1)*(p3-1) 
                if digits_of(phi) == digits_of(p1*p2*p3):
                    if p1*p2*p3 > m:
                        m = p1*p2*p3
                        print(m)
