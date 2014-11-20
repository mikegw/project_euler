c = 1
for j in range(101):
    for k in range(41):
        for l in range(21):
            for m in range(11):
                for n in range(5):
                    for o in range(3):
                        if 2*j + 5*k + 10*l + 20*m + 50*n + 100*o <= 200:
                            c += 1

print(c)
