def brute():
    squares = [i**2 for i in range(1,500)]
    perimeters = [0]*1001
    for b in range(1,500):
        for a in range(1,b):
            c2 = a**2 + b**2
            if c2 in squares:
                c = int(c2**0.5)
                #print(a,b,c, a+b+c)
                if a+b+c < 1001:
                    perimeters[a+b+c] += 1
    m = (0,0)
    for i in range(1,1001):
        if perimeters[i] > m[1]:
            m = (i,perimeters[i])
    print(m)

brute()

        
