def brute():
    t = 0
    found = False
    for i in range(1,100000):
        t += i
        c = 0
        for j in range(1,t):
            if t % j == 0:
                c += 1
                if c > 499:
                    print(i,t)
                    found = True
                    break
    if not found:
        print("Nope")

def simpleseive(n):
    A = [1]*n
    for i in range(2,int(n**0.5)):
        if A[i] == 1:
            for j in range(i**2,n,i):
                A[j] = 0
    B = [i*A[i] for i in range(2,n) if A[i] == 1]

    return(B)


def twelve(n):
    t = 0
    primes = simpleseive(1000)
    print(primes)
    found = False
    for i in range(1,n):
        t += i
        no_of_factors = 1
        for power in range(1000):
            if i % (2**power) != 0:
                #print(i, " not divisible by ", 2, " ^ ", power)
                no_of_factors *= power
                break
        for power in range(1000):
            if (i+1) % (2**power) != 0:
                #print(i+1, " not divisible by ", 2, " ^ ", power)
                no_of_factors *= power
                break
        no_of_factors -= 1

        for p in primes[1:]:
            if p <= i:
                for power in range(1000):
                    if i % (p**power) != 0:
                        #print(i, " not divisible by ", p, " ^ ", power)
                        no_of_factors *= power
                        break
                for power in range(1000):
                    if (i+1) % (p**power) != 0:
                        no_of_factors *= power
                        #print(i+1, " not divisible by ", p, " ^ ", power)
                        break
            else:
                break
        if no_of_factors > 499:
            print(i,t)
            break
        


twelve(100000)
