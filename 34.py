from functions import factorial as f

print(8*f(9))

def factsum(n):
    l_n = [int(str(n)[i]) for i in range(len(str(n)))]
    return(sum([f(i) for i in l_n]))

ans = 0
for i in range(3,300000):
    if factsum(i) == i:
        print(i)
        ans += i
print(ans)
