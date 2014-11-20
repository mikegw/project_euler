def pb45():
    for n in range(100000):
        h = n*(2*n-1)
        if (1 + 24*h)**0.5 % 6 == 5:
            if (1 + 8*h)**0.5 % 2 == 1:
                print(h)

pb45()
