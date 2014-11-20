from functions import lex_up, lex_to_int

lex = [0,0,0,0,-1,0,0,0]
values = set([])

#for i in range(120):
#    lex_up(lex)
#    print(lex)
#    print(lex_to_int(lex))

for i in range(15120):
    lex_up(lex,4)
    s = str(lex_to_int(lex))
    l = [int(s[i]) for i in range(5)]
    #print(lex,l)
    p = (100*l[0]+10*l[1]+l[2])*(10*l[3]+l[4])
    plist = [int(str(p)[i]) for i in range(len(str(p)))]
    pset = set(plist)
    if len(pset) == len(plist) and pset.isdisjoint(set(l).union(set([0]))):
        print(p,pset,plist,l)
        values.add(p)
    q = (1000*l[0]+100*l[1]+10*l[2]+l[3])*(+l[4])
    qlist = [int(str(q)[i]) for i in range(len(str(q)))]
    qset = set(qlist)
    if len(qset) == len(qlist) and qset.isdisjoint(set(l).union(set([0]))):
        print(q,qset,qlist,l)
        values.add(q)

print(values)
print(sum(values))


