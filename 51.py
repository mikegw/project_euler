from functions import simpleseive


#for p in primes:
    #print(p)
A = simpleseive(10000000, t = False)
print('primed')

for n in range(1000000,2000000):
    s = str(n)
    l = len(s)-1
    for i in range(l-3):
        for j in range(i+1,l-2):
            for k in range(j+1,l-1):
                pn = []
                if i == 0:
                    c = 1
                else:
                    c = 2
                for d in range(1,10):
                    s = s[:i]+str(d)+s[i+1:j]+str(d)+s[j+1:k]+str(d)+s[k+1:]
                    if int(s) % 3 != 0:
                        if A[int(s)]:
                            pn.append(int(s))
                        else:
                            c -= 1
                            if c == 0:
                                break
                    else:
                        break
                else:
                    print(pn)
