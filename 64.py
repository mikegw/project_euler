def cf(n):
    cfs = [[int(n**0.5),int(n**0.5),1]]
    #print(cfs)
    for i in range(1000):
        a = int(cfs[-1][2]/(n**0.5 - cfs[-1][1]))
        c = (n - cfs[-1][1]**2)/cfs[-1][2]
        b = a*c - cfs[-1][1]
        new = [a,b,c]
        #print(new)
        if i > 0 and new == cfs[1]:
            #print([it[0] for it in cfs])
            return len(cfs)-1
            break
        else:
            cfs.append(new)
                
    
    

c = 0




for n in range(2,10001):
    if n**0.5 % 1 != 0:
        if cf(n) % 2 == 1:
            print(n)
            c += 1

print(c)
