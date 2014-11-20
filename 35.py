from functions import simpleseive

def rotate(n,by):
    l_n = [i for i in str(n)]
    l_r = l_n[by:]+l_n[:by]
    r = ''
    for i in l_r:
        r += i
    return int(r)

def pb35(n):
    ans = 0
    l = []
    primes = simpleseive(n)
    for p in primes[4:]:
        if sum([['2','4','5','6','8','0'].count(i) for i in str(p)]) == 0:
            circ = True
            for i in range(1,len(str(p))):
                if not rotate(p,i) in primes:
                    #print(rotate(p,i))
                    circ = False
                    break
            if circ:
                ans += 1
                l.append(p)

    print(l)
    print(ans+4)

pb35(1000000)
        
        
