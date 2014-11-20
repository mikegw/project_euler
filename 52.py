def brute():
    for n in range(100000,10000000):
        for i in range(2,7):
            if set(str(i*n)) != set(str(n)):
                break
        else:
            print(n,2*n,3*n,4*n,5*n,6*n)

brute()
