def six():
    s1 = sum(i**2 for i in range(1,101))
    s2 = (101*50)**2
    print(s1,s2,s2-s1)

six()
