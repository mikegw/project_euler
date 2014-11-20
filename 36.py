def bin_up(b):
    b[0] += 1
    for i in range(len(b)-1):
        if b[i] == 2:
            b[i] = 0
            b[i+1] += 1
    if b[-1] == 2:
        for i in range(len(b)):
            b[i] = 0
        b.append(1)

def bin_to_int(b):
    return sum([b[i]*2**i for i in range(len(b))])#

def is_palindrome(n):
    s = str(n)
    if len(s) % 2 ==1:
        return s[:len(s)/2] == s[:len(s)/2:-1]
    else:
        return s[:len(s)/2] == s[:len(s)/2-1:-1]

def pb36():
    values = []
    b = [1]
    for i in range(1024):
        b1 = b[::-1] + b[1:]
        b2 = b[::-1] + b
        n1 = bin_to_int(b1)
        n2 = bin_to_int(b2)
        if is_palindrome(n1):
            values.append(n1)
        if is_palindrome(n2):
            values.append(n2)
        bin_up(b)

    print(values,sum([v for v in values if v < 1000000]))

pb36()
        



