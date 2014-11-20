from functions import *

def abundantsl(n):
    abundants = []
    for i in range(1,n):
        if sum_of_proper_factors_of(i) > i:
            abundants.append(i)
    #print(abundants)
    return(abundants)

def pb23(n):
    abundants = abundantsl(n)
    A = [False]*n
    for i in range(len(abundants)):
        for j in range(i+1):
            s = abundants[i] + abundants[j]
            if s < n:
                A[s] = True

    print(sum([i*(not(A[i])) for i in range(len(A))]))

pb23(28124)



