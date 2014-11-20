fractions = []

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if k != j:
                if float(10*i+j)/(10*k+i) == float(j)/k:
                    fractions.append((10*i+j,10*k+i))
                if float(10*j+i)/(10*i+k) == float(j)/k:
                    fractions.append((10*j+i,10*i+k))

print([f for f in fractions if f[0]<f[1]])
