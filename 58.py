from functions import simpleseive

primes = simpleseive(100000,2)

def layer(n):
    return range((2*n-1)**2 + 1,(2*n+1)**2 + 1)

def diagonals(n):
    return [(2*n+1)**2 - 6*n, (2*n+1)**2 - 4*n, (2*n+1)**2 - 2*n]


def pb58(n):
    pds = []
    for i in range(1,n):
        diags = diagonals(i)
        for d in diags:
            rd = int(d**0.5)
            for p in primes:
                if p >= rd:
                    pds.append(d)
                    break
                elif d % p == 0:
                    break
        if 10*len(pds) < 4*i-3:
            print(len(pds),4*i - 3, 2*i - 1)
            return

pb58(100000)


