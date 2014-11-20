def nine():
    for b in range(500):
        for a in range(b):
            if a**2 + b**2 == (1000-a-b)**2:
                print(a,b,1000-a-b,a*b*(1000-a-b))

nine()
