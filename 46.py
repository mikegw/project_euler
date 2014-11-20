from functions import simpleseive



def pb46():
    primes = simpleseive(800000)
    print('Primes')
    odds = [False]*2000000
    for s in range(1200):
        print(s)
        s2 = s**2
        for p in primes:
            if p + 2*s2 < 2000000:
                odds[p + 2*s2] = True
    for i in range(1000000):
        odds[2*i] = True
    for j in range(2000000):
        if not odds[j]:
            print(j)    


pb46()
