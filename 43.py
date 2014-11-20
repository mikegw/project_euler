from functions import lex_up as up
from functions import lex_to_int as num

primes = [2,3,5,7,11,13,17]

def pb43():
    ans = 0
    l = [1,0,0,0,0,0,0,0,0]
    while l != [9,8,7,6,5,4,3,2,1]:
        n = num(l,0)
        s = str(n)
        for i in range(7):
            #print(s,int(s[i+1:i+4]),primes[i],int(s[i+2:i+5]) % primes[i])
            if int(s[i+1:i+4]) % primes[i] != 0:
                break
        else:
            print(n)
            ans += n
        #return
        up(l)
    print(ans)


pb43()
