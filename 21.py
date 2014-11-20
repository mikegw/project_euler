def simpleseive(n):
    A = [1]*n
    for i in range(2,int(n**0.5)):
        if A[i] == 1:
            for j in range(i**2,n,i):
                A[j] = 0
    B = [i*A[i] for i in range(2,n) if A[i] == 1]

    return(B)

primes = simpleseive(100000)

def product(list):
    p = 1
    for n in list:
        p *= n
    return p

def factors_of(n):
    if n == 1:
        return[0]
    else:
        pfactors = []
        n1 = n
        for i in range(len(primes)):
            p = primes[i]
            if p > n or n1 == 1:
                break
            pfactors.append(0)
            while n1 % p == 0:
                pfactors[i] += 1
                n1 = n1/p
        #print(pfactors)
        factors = []
        it = [0]*len(pfactors)
        while it[-1] <= pfactors[-1]:
            #print(it)
            #print([primes[j]**it[j] for j in range(len(pfactors))])
            factors.append(product([primes[j]**it[j] for j in range(len(pfactors))]))
            it[0] += 1
            for k in range(len(pfactors)-1):
                if it[k] > pfactors[k]:
                    it[k] = 0
                    it[k+1] += 1
        return(factors)

def proper_factors_of(n):
    return factors_of(n)[:-1]

def sum_of_proper_factors(n):
    #primes = simpleseive(100000)
    factors = proper_factors_of(n)
    return(sum(factors))

def pb21():
    l = range(2,10000)
    ans = 0
    for a in l:
        #print("a=",a)
        b = sum_of_proper_factors(a)
        #print("b=",b)
        if sum_of_proper_factors(b) == a:
            print(a,b)
            if a != b:
                ans += a + b
                l.remove(b)
            else:
                print(a)
    print(ans)
pb21()
        
        
