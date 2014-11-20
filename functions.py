def simpleseive(n,start = 0, t = True):
    A = [1]*n
    for i in range(2,int(n**0.5)):
        if A[i] == 1:
            for j in range(i**2,n,i):
                A[j] = 0
    if t:
        return [i*A[i] for i in range(start,n) if A[i] == 1]
    else:
        return A[start:]

def is_prime(n, primes):
    n1 = int(n**0.5)
    for p in primes:
        if p >= n1:
            return True
        elif n % p == 0:
            return False
    

primes = simpleseive(100000)

def is_palindrome(x):
    return str(x) == str(x)[::-1]

def reverse_int(x):
    return int(str(x)[::-1])

def product(list):
    p = 1
    for n in list:
        p *= n
    return p

def where_is_first(n,l):
    for i,x in enumerate(l):
        #print(i,x)
        if x == n:
            return(i)
    return(None)

def factorial(x):
    i = 1
    for j in range(1,x+1):
        i *= j
    return(i)

def sumdigits(n):
    x = 0
    for i in str(n):
        x += int(i)
    return x

def rotate(n,by):
    l_n = [i for i in str(n)]
    l_r = l_n[by:]+l_n[:by]
    r = ''
    for i in l_r:
        r += i
    return int(r)

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

def sum_of_proper_factors_of(n):
    #primes = simpleseive(100000)
    factors = proper_factors_of(n)
    return(sum(factors))



def lex_up(lex,by = 1):
    #test it is a lex
    #for i in range(len(lex)):
    #    if lex(i) > i+1:
    #        print("Not a lex")
    #        return(None)
    lex[-by] +=1
    for i in range(by,len(lex)+1):
        if lex[-i] == i + 1:
            lex[-i-1] += 1
            lex[-i] = 0
    return lex

def lex_down(lex,by = 1):
    lex[-by] -=1
    for i in range(by,len(lex)+1):
        if lex[-i] == -1:
            lex[-i-1] -= 1
            lex[-i] = i
    return lex

def permute(n,lex):
    l = lex + [0]
    s = str(n)
    digits = [int(d) for d in s]
    no_of_digits = len(digits)
    #l.reverse()
    ordered_digits = []
    for i in range(no_of_digits):
        #print("Ordered: ", ordered_digits)
        #print("Digits: ", digits)
        ordered_digits.append(digits[l[i]])
        digits.remove(digits[l[i]])
    ordered_digits.reverse()
    return sum([ordered_digits[i]*(10**i) for i in range(len(ordered_digits))])

def permute_list(pl,lex):
    l = lex + [0]
    digits = pl + []
    no_of_digits = len(digits)
    #l.reverse()
    ordered_digits = []
    for i in range(no_of_digits):
        #print("Ordered: ", ordered_digits)
        #print("Digits: ", digits)
        ordered_digits.append(digits[l[i]])
        digits.remove(digits[l[i]])
    ordered_digits.reverse()
    return ordered_digits
    

def lex_to_int(lex,start=1):
    l = lex + [0]
    digits = [i for i in range(1,len(l)+1)]
    no_of_digits = len(digits)
    #l.reverse()
    ordered_digits = []
    for i in range(no_of_digits):
        #print("Ordered: ", ordered_digits)
        #print("Digits: ", digits)
        ordered_digits.append(digits[l[i]]-(1-start))
        digits.remove(digits[l[i]])
    ordered_digits.reverse()
    return sum([ordered_digits[i]*(10**i) for i in range(len(ordered_digits))])

def modexp(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if (exponent % 2 == 1):
           result = (result * base) % modulus
        exponent = exponent / 2
        base = (base * base) % modulus
    return result
