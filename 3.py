def factor(n):
    factors = []
    primes = [2,3,5]
    for i in range(2,int(n**0.5)):
        prime = True
        for p in primes:
            if i % p == 0:
                prime = False
                break
        if prime:
            primes.append(p)

def brute(n):
    factors = []
    factors2 = []
    for i in range(2,int(n**0.5)):
        if n % i == 0:
            factors.append(i)
    for f in factors:
        f2 = []
        for j in range(2,f):
            if f % j == 0:
                f2.append(j)
        factors2.append(f2)
            
    

    print(factors)
    print(factors2)

brute(600851475143)
