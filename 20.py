def fact(n):
    x = 1
    for i in range(1,n+1):
        x *= i
    return x

def sumdigits(n):
    x = 0
    for i in str(n):
        x += int(i)
    return x

print(fact(100))
print(sumdigits(fact(100)))
