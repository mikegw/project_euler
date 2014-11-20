from functions import lex_up as up, permute_list as perm

inner = []
outer = []

def check_sums(l):
    sums = []
    for i in range(1,len(l)):
        s = l[i]+l[(i+1) % len(l)]
        if s in sums:
            return False
        else:
            sums.append(s)
    return True
    



for i1 in range(5,10):
    for i2 in range(4,i1):
        for i3 in range(3,i2):
            for i4 in range(2,i3):
                for i5 in range(1,i4):
                    inner = [i1,i2,i3,i4,i5]
                    lex = [0,0,0,-1]
                    while lex != [4,3,2,1]:
                        up(lex)
                        trial = perm(inner,lex)
                        if check_sums(trial):
                            #print(trial)
                            unused = set([1,2,3,4,5,6,7,8,9,10]) - set(inner)
                            u = min(unused)
                            s = trial[0] + trial[1] + u
                            outer = [u,s-(trial[1]+trial[2]),s-(trial[2]+trial[3]),
                                        s-(trial[3]+trial[4]),s-(trial[4]+trial[0])]
                            #print(trial,outer)
                            if set(outer+inner) == set([1,2,3,4,5,6,7,8,9,10]):
                                rep = []
                                for i in range(5):
                                    rep += [outer[i],trial[i],trial[(i+1)%5]]
                                rep = [str(r) for r in rep]
                                s = ''
                                for r in rep:
                                    s += str(r)
                                s = int(s)
                                print(trial,outer,s)
                                #print('WINNER, WINNER, CHICKEN DINNER')                                
                    
