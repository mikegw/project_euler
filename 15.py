def f(x):
    i = 1
    for j in range(1,x+1):
        i *= j
    return(i)

print(f(3))
print(f(5))

print(f(40)/(f(20)**2))


