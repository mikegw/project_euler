scubes = [str(i**3) for i in range(1000)]
ccubes = [[s.count(i) for i in range(10)] for s in scubes]

for c in ccubes:
    if ccubes.count(c) == 5:
        print(c)
        print([s for s in scubes if [s.count(i) for i in range(10)] == c])

