def cf(x,n):
    i = 0
    cf = [int(x)]
    alpha = x - int(x)
    while i < n: 
        if alpha != 0:
            a = int(1/ alpha)
            alpha = 1/alpha - int(1/ alpha)
            if [a,int(1000*alpha)] not in cf:
                cf.append([a,int(1000000*alpha)])
                i += 1
            else:
                break
        else:
            break
    return(i)
#    cf.reverse()
#    value = cf[0]
#    for i in range(1, len(cf)):
#        value = cf[i] + 1/ value

#   print(value)

