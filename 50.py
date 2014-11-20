from functions import simpleseive

primes1 = simpleseive(1000000)
primes2 = simpleseive(10000)

#print(sum([primes1[i] for i in range(546)]))

print(primes2)

i = 546
while i > -1:
    j = 547 - i
    while j > -1:
        #print(primes2[j:i+j])
        if sum(primes2[j:i+j]) in primes1:
            print(primes2[j:i+j],sum(primes2[j:i+j]))
            j = 0
            i = 0
        j = j-1
    i = i-1
