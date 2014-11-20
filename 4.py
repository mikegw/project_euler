def four():
    m = 1
    for i in range(100,1000):
        for j in range(100,1000):
            if i*j == int(str(i*j)[::-1]) and i*j > m:
                m = i*j
                print(i,j,m)
                

four()
