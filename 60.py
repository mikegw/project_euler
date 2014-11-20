from functions import simpleseive as s, is_prime
from time import clock as now

primes1 = s(9000,2)
primes2 = s(10000,2)

def test(list_of_primes):
    for i in range(len(list_of_primes)):
        for j in range(i + 1,len(list_of_primes)):
            if not is_prime(int(str(list_of_primes[i]) + str(list_of_primes[j])),primes2) or not is_prime(int(str(list_of_primes[j]) + str(list_of_primes[i])),primes2):                
                return False
    else:
        return True   
                 
#for i in range(4,len(primes1)):
#    print(i)
#    for j in range(3,i):
#        for k in range(2,j):
#            for l in range(1,k):
#                for m in range(l):
#                    if test([primes1[i],primes1[j],primes1[k],primes1[l],primes1[m]]):
#                        print([primes1[i],primes1[j],primes1[k],primes1[l],primes1[m]], sum([primes1[i],primes1[j],primes1[k],primes1[l],primes1[m]]))

n = now()




def pb60():
    c=0
    pairs = []
    triples = []
    for i in range(1,len(primes1)):
        for j in range(i):
            if test([primes1[i],primes1[j]]):
                c+=1
                recent = [primes1[i],primes1[j]]
                pairs.append(recent)
                for pair in pairs[:-1]:
                    if recent[1] < pair[0]:
                        break
                    elif recent[1] == pair[0]:
                        if test([recent[0],pair[1]]):
                            recent_t = recent + [pair[1]]
                            triples.append(recent_t)
                            #print(recent_t)
                            for t in triples[:-1]:
                                if recent_t[-1] < t[0]:
                                    break
                                elif recent_t[-1] == t[0]:
                                    if test(recent_t[:-1] + t):
                                        print(recent_t[:-1] + t)
                                        print(sum(recent_t[:-1] + t))
                                        #return

pb60()

#print(len(pairs))
#
#print(now() - n)
#
#
#for i in range(1,len(pairs)):
#    for j in range(i):
#        if pairs[i][1] < pairs[j][0]:
#            break
#        elif pairs[i][1] == pairs[j][0]:
#            if test([pairs[i][0],pairs[j][1]]):
#                triples.append([pairs[i][0],pairs[i][1],pairs[j][1]])
#            break
#
#print(len(triples))
#
#print(now() - n)
#
#for i in range(1,len(triples)):
#    for j in range(i):
#        if triples[i][-1] < triples[j][0]:
#            break
#        elif triples[i][-1] == triples[j][0]:
#            if test(triples[i][:-1] + triples[j]):
#                print(triples[i][:-1] + triples[j])
#            break
#
#print(now() - n)
