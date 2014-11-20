def brute():
    prod = 1
    count = 0
    n = 1
    for i in range(1,1000000):
        s = str(i)
        for j in s:
            count += 1
            if count == n:
                prod *= int(j)
                print(n)
                n = 10*n
                if n == 10000000:
                    print(prod)
                    return

brute()
