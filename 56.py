from functions import sumdigits 

current = 0

for a in range(100):
    for b in range(100):
        if sumdigits(a**b) > current:
            current = sumdigits(a**b)

print(current)
