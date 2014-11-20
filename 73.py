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

def phi3(n):
    '''Yuck'''
    l = [1]*n
    for i in range(2,n):
        if n % i == 0 or i == 3:
            for j in range(0,n,i):
                l[j] = 0
    return sum(l)


def phi_without3(n):
    if n % 3 == 0:
        return phi(n)
    elif n % 3 == 1:
        return 2*phi(n)/3
    else:
        return 2*(phi(n)+1)/3

def sum_without3(n):
    s = 0
    for i in range(4,n+1):
        s += phi_without3(i)
    return s

def sum_phi(n):
    s = 0
    for i in range(4,n+1):
        s += phi(n)
    return s

s1 = sum_phi(12000)
print(s1)
s2 = (s1 - 1)/2
print(s2)
s3 = s1 - sum_without3(12000) + sum_without3(4000)
print(s3)
s4 = s2 - 1 -s3
print(s4)
print(2*s4 + 2*s3)

#for i in range(2,100):
#    print(phi3(i)-phi_without3(i))
    
