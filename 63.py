from time import clock as now

start = now()
nmax = 0
m = 1
while m >= 0.1:
    nmax += 1
    m *= 0.9

print(len([i**j for i in range(1,10) for j in range(nmax) if len(str(i**j)) == j]))
print(now()-start)
