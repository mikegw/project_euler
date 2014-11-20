from functions import factorial as f

def choose(n,r):
    return f(n)/(f(r)*f(n-r))

def brute():
    c = 0
    for n in range(23,101):
        for r in range(n):
            if choose(n,r) >= 1000000:
                c += 1
    print(c)
brute()
