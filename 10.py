import copy

def ten():
    primes = [2,3,5]
    i = 7
    while primes[-1] < 2000000:
        prime = True
        for p in primes:
            if i % p == 0:
                prime = False
                break
        if prime:
            primes.append(i)
        i += 2
        if i % 1000 == 1:
            print(i)
    print(sum(primes[0:-1]))

def seive():
    primes = [2,3,5,7,11]
    s = []
    s2 = []
    for i in range(3,200):
        co = True
        for p in primes:
            if i % p ==0:
                co = False
        if co == True:
            s.append(i)
            s2.append(i)
    print(s2)

    while len(s) > 1:
        print("new = ", s[0])
        primes.append(s[0])
        for k in s:
            if k % s2[0] == 0:
                print(k)
                s2.remove(k)
                
        s = copy.deepcopy(s2)
        print(s)

    print(sum(primes[0:-1]))

def simpleseive(n):
    A = [1]*n
    for i in range(2,int(n**0.5)):
        if A[i] == 1:
            for j in range(i**2,n,i):
                A[j] = 0
    B = [i*A[i] for i in range(n)]
    print(B)

simpleseive(2000000)
