from functions import is_palindrome as isp
from functions import reverse_int as rint

def is_lychrel(n):
    x = n*1
    for i in range(49):
        x = x + rint(x)
        if isp(x):
            return False
    else:
        return True

print(is_lychrel(1000))

print(is_lychrel(196))

def pb55():
    c = 0
    for n in range(1,10000):
        if is_lychrel(n):
            c += 1
    print(c)

pb55()
