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

e = [2]
for i in range(1,35):
    e += [1,2*i,1]


e = e[:100]

e = e[::-1]

frac = Fraction(1,0)

for i in e:
    frac = Fraction(i,1) + Fraction(1,1)/frac

print(sumdigits(frac.n))
