def seven():
    primes = [2,3,5]
    i = 6
    while len(primes) < 10001:
        prime = True
        for p in primes:
            if i % p == 0:
                prime = False
                break
        if prime:
            primes.append(i)
        i += 1
    print(primes)

seven()
