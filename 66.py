from functions import simpleseive, sumdigits

primes = simpleseive(10000,2)

class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.reduce()

    def reduce(self):
        for p in primes:
            if p < self.n and p < self.d:
                while self.n % p == 0 and self.d % p == 0:
                    self.n , self.d = self.n/p, self.d/p

    def __add__(self,other):
        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return Fraction(n,d)

    def __div__(self,other):
        n = self.n*other.d
        d = self.d*other.n
        return Fraction(n,d)

    def __repr__(self):
        return str([self.n,self.d])

def f_sol(D):
    cfs = [[int(D**0.5),int(D**0.5),1]]
    cvgs = []
    #print(cfs)
    for i in range(10000):
        a = int(cfs[-1][2]/(D**0.5 - cfs[-1][1]))
        c = (D - cfs[-1][1]**2)/cfs[-1][2]
        b = a*c - cfs[-1][1]
        new = [a,b,c]
        cfs.append(new)
        #print(new)
        l = len(cfs)
        frac = Fraction(1,0)
        for j in range(l):
            frac = Fraction(cfs[l-j-1][0],1) + Fraction(1,1)/frac
        if frac.n**2 - D*frac.d**2 == 1:
            return (frac.n,frac.d)
            break
        else:
            pass


def pb_66():
    m = 0
    d = 0
    for D in range(2,1001):
        print(D)
        if D**0.5 % 1 != 0:
            f = f_sol(D)
            if f > m:
                m = f
                d = D            
    print(d,m)

pb_66()


