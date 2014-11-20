from functions import *
from time import clock as now

n = now()

lex = [8,7,6,5,4,3,2,1]
while lex != [0,0,0,0,0,0,0,0]:
    lex_down(lex)
    l = str(lex_to_int(lex))
    if int(l[:4])*2 == int(l[4:]):
        print(l)
        break
    elif int(l[:1])*2 == int(l[1:3]) and int(l[:1])*2 == int(l[3:5]) and int(l[:1])*4 == int(l[5:7]) and int(l[:1])*2 == int(l[7:]):
        print(l)
        break
print(now()-n)
print('Done')
