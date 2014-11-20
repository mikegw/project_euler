from functions import modexp
from time import clock as now

n = now()
ans = 0
for i in range(1,1001):
    ans = ans + modexp(i,i,10000000000) % 10000000000
print(ans)
print(now()-n)

print(modexp(1001,1001,10000000000))
