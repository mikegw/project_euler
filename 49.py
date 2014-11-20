from functions import simpleseive, rotate

primes = simpleseive(10000)

for i in range(1001,10000):
    if str(i).count('0') == 0:
        if i in primes:
            for p1 in primes:
                if p1 > i and set(str(i)) == set(str(p1)):
                    p2 = 2*p1 - i
                    if p2 > i and p2 in primes and set(str(i)) == set(str(p2)):
                        print(i,p1,p2)
                        
