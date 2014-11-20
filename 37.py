from functions import simpleseive as seive
def pb37():
    trunc_primes = []
    for i in range(2,7):
        print('i = ' + str(i))
        primes = seive(10**i)
        #print(primes)
        print('Seived')
        for p in primes:
            if p < 10**(i-1):
                pass
            elif ['3','7'].count(str(p)[-1]) == 0:
                pass
            elif ['0','2','4','5','6','8'].count(str(p)[1:]) > 0:
                pass
            else:
                trunc = True
                for j in range(1,len(str(p))):
                    if not p % 10**j in primes:
                        trunc = False
                        break
                    if not p / 10**j in primes:
                        trunc = False
                        break
                if trunc:
                    trunc_primes.append(p)
                    print(trunc_primes)
                    if len(trunc_primes) == 11:
                        return(sum(trunc_primes))

print(pb37())
