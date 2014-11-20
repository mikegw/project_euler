def is_tri(n):
    return (1 + 8*n)**0.5 % 2 == 1

def is_sq(n):
    return n**0.5 % 1 == 0

def is_pent(n):
    return (1 + 24*n)**0.5 % 6 == 5

def is_hex(n):
    return (1 + 8*n)**0.5 % 4 == 3

def is_hept(n):
    return (9 + 40*n)**0.5 % 10 == 7

def is_oct(n):
    return (1 + 3*n)**0.5 % 3 == 2

def new_rep(n,l):
    if 't' not in l and is_tri(n):
        #l.append('t')
        return True
    elif 'sq' not in l and is_sq(n):
        #l.append('sq')
        return True
    elif 'p' not in l and is_pent(n):
        #l.append('p')
        return True
    elif 'hx' not in l and is_hex(n):
        #l.append('hx')
        return True
    elif 'hp' not in l and is_hept(n):
        #l.append('hp')
        return True
    elif 'o' not in l and is_oct(n):
        #l.append('o')
        return True
    else:
        return False

def list_reps(n):
    l = []
    if is_tri(n):
        l.append('t')
    if 'sq' not in l and is_sq(n):
        l.append('sq')
    if 'p' not in l and is_pent(n):
        l.append('p')
    if 'hx' not in l and is_hex(n):
        l.append('hx')
    if 'hp' not in l and is_hept(n):
        l.append('hp')
    if 'o' not in l and is_oct(n):
        l.append('o')
    return l

full = set([i for i in range(1000,10000) if i % 100 > 9 and 
    (is_tri(i) or is_sq(i) or is_pent(i) or
     is_hex(i) or is_hept(i) or is_oct(i))])




d2 = set([i % 100 for i in full])
d2 = range(10,100)

def pb61():
    for n1 in full:
        l1 = []
        m1 = list_reps(n1)        
        for i1 in m1:
            if i1 not in l1:
                l2 = l1 + [i1]            
                for n2 in d2:
                    m2 = list_reps(100*(n1 % 100) + n2)
                    for i2 in m2:
                        if i2 not in l2:
                            l3 = l2 + [i2]
                            for n3 in d2:
                                m3 = list_reps(100*n2 + n3)
                                for i3 in m3:
                                    if i3 not in l3:
                                        l4 = l3 + [i3]
                                        for n4 in d2:
                                            m4 = list_reps(100*n3 + n4)
                                            for i4 in m4:
                                                if i4 not in l4:
                                                    l5 = l4 + [i4]
                                                    for n5 in d2:
                                                        m5 = list_reps(100*n4 + n5)
                                                        for i5 in m5:
                                                            if i5 not in l5:
                                                                l6 = l5 + [i5]
                                                                m6 = list_reps(100*n5 + n1/100)
                                                                for i6 in m6:
                                                                    if i6 not in l6:
                                                                        print(n1,100*(n1 % 100) + n2,100*n2 + n3,100*n3 + n4,100*n4 + n5,100*n5 + n1/100)
                                                                        print(sum([n1,100*(n1 % 100) + n2,100*n2 + n3,100*n3 + n4,100*n4 + n5,100*n5 + n1/100]))
                                                                        return

pb61()

#print('l' not in [] and True)
                

