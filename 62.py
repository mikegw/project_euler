from functions import permute
from functions import lex_up as up
from time import clock as now

cubes = [i**3 for i in range(1000)]

for c in cubes:
    cps = set([c])
    l = len(str(c))-1
    lex = [0]*l
    fin = [l-j for j in range(l)]
    while lex != fin:
        up(lex)
        n = permute(c,lex)
        if n in cubes and len(str(n)) == l + 1:
            cps.add(n)
            print(cps)
    if len(cps) == 5:
        print(cps)
