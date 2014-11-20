from functions import simpleseive
from time import clock as now

strs = {0:[''], 1:['0','1','2','3','4','5','6','7','8','9']}
strs0 = {0:[''], 1:['1','2','3','4','5','6','7','8','9']}

strs[2] = [i+j for i in strs[1] for j in strs[1]]
strs[3] = [i+j for i in strs[1] for j in strs[2]]
strs[4] = [i+j for i in strs[1] for j in strs[3]]
#strs[5] = [i+j for i in strs[1] for j in strs[4]]
#strs[6] = [i+j for i in strs[1] for j in strs[5]]

strs0[2] = [i+j for i in strs0[1] for j in strs[1]]
strs0[3] = [i+j for i in strs0[1] for j in strs[2]]
strs0[4] = [i+j for i in strs0[1] for j in strs[3]]
#strs0[5] = [i+j for i in strs0[1] for j in strs[4]]
#strs0[6] = [i+j for i in strs0[1] for j in strs[5]]

smallprimes = simpleseive(100,2)

def isprime(n):
    for p in smallprimes:
        if n % p == 0:
            return False
    else:
        for i in range(2,int(n**0.5 / 6)):
            if n % (6*i - 1) == 0 or n % (6*i + 1) == 0:
                return False
        else:
            return True

#start = now()
#for n in range(100000000):
#    isprime(n)

#print(now()-start)



def pb51(end):
    for l in range(5,end):
        
        for i in range(l-3):
            for j in range(i+1,l-2):
                for k in range(j+1,l-1):
                    for n1 in strs0[i]:
                        for n2 in strs[j-i-1]:
                            for n3 in strs[k-j-1]:
                                for n4 in strs[l-k-1]:
                                    ln = []
                                    for r in range(10):
                                        sr = str(r)
                                        s = n1 + sr + n2 + sr + n3 + sr + n4
                                        n = int(s)
                                        if isprime(n):
                                            ln.append(n)
                                            if len(ln) > 7:
                                                print(ln)
                                                print(sum(ln))
                                                #return
                                            
                                    

n = now()
pb51(9)
print(now()-n)










