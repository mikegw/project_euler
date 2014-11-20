from functions import simpleseive

primes = simpleseive(10000,2)

class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.v = float(n)/d
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

c = Fraction(2,5)

for d in range(2,1000001):
    if d % 7 != 0:
        n = 3*d/7
        f = Fraction(n,d)
        if f.v > c.v:
            print(f)
            c = f

print c

