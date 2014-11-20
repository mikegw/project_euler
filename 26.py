from functions import where_is_first
from time import clock as now

def f(x):
    remainders = []
    denominator = []
    numerator = 1
    while True:
        d = numerator / x
        denominator.append(d)
        r = numerator % x
        #print(numerator, r)
        if r in remainders:
            return(len(remainders)-where_is_first(r,remainders))
            #print(denominator)
            #remainders.append(r)
            #print(remainders)
            
            break
        remainders.append(r)
        numerator = r*10


def pb26(n):
    print(now())
    m = (0,0)
    for i in range(2,n):
        if f(i) > m[1]:
            m = (i,f(i))
    print(m)
    print(now())

pb26(1000)
