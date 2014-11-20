from functions import lex_down as d, lex_to_int as i, simpleseive as s
from time import time as now

primes = s(10000)

def brute():
    for k in range(3):
        lex = [6-k-j for j in range(6-k)]
        while lex != [0]*(6-k):
            l_k = i(lex)
            for p in primes:
                if l_k % p == 0 and l_k > p:
                    break
            else:
                print(l_k)
                return
            d(lex)

n = now()       
brute()
print(now()-n)
    
