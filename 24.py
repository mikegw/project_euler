def increment_lex(lex):
    #test it is a lex
    #for i in range(len(lex)):
    #    if lex(i) > i+1:
    #        print("Not a lex")
    #        return(None)
    lex[0] +=1
    for i in range(len(lex)):
        if lex[i] == i + 1:
            lex[i+1] += 1
            lex[i] = 0
    return lex

def lex_to_int(lex):
    l = [0] + lex
    digits = [i for i in range(len(l))]
    no_of_digits = len(digits)
    #l.reverse()
    ordered_digits = []
    for i in range(no_of_digits):
        #print("Ordered: ", ordered_digits)
        #print("Digits: ", digits)
        ordered_digits.append(digits[l[i]])
        digits.remove(digits[l[i]])
    ordered_digits.reverse()
    return sum([ordered_digits[i]*(10**i) for i in range(len(ordered_digits))])

lex = [0,0,0,0,0]

#for j in range(100):
#    print('lex: ', lex)
#    print('int: ', lex_to_int(lex))
#    increment_lex(lex)

def pb24(n):
    lex = [0,0,0,0,0,0,0,0,0]

    for j in range(n-1):
        increment_lex(lex)

    print(lex)
    print(lex_to_int(lex))
pb24(1000000)
