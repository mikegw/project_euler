def pb44():
    pent = []
    for n in range(1,10000):
        pn = n*(3*n-1)/2
        for p in pent:
            s = pn + p
           # print(pn,p,s)
            if (1 + 24*s)**0.5 % 6 == 5:
                d = pn - p
                if (1 + 24*d)**0.5 % 6 == 5:
                    print(p,pn,d)
        pent.append(pn)
        #print(pent)

pb44()
