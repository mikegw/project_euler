from time import clock as now
from functions import factorial as f

def sumfact(n):
    s = str(n)
    return sum([f(int(i)) for i in s])

l = [0]*3000000

def pb74(n,prev):
    #print(len(l))
    p = prev
    if l[n] != 0:
        print l[n]
        return l[n]
    else:
        m = sumfact(n)
        #print "\t", n,m
        if m == p[0]:
            l[m] = 3
            #print(l[m])
            #print 3
            return 3
        elif m == p[1]:
            l[m] = 2
            #print(l[m])
            #print 2
            return 2
        elif m == n:
            return 1
        else:
            new = pb74(m,p[1:]+[n])
            #print(n, new,sum([i*l[i] for i in l]))
            l[n] = new + 1
            return l[n]

for i in range(1,200):
    print(i, pb74(i,[0,0,0]))

