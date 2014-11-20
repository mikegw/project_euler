def pb14():
    prev = {1:0}
    for i in range(2,1000000):
        c = 0

        t = i
        #print("Start: ",i)
        while True:
            #print(t)
            c += 1
            if t % 2 == 0:
                t = t/2
            else:
                t = 3*t+1
            if t in prev:
                #print(i,t,c,prev)
                prev[i] = prev[t] + c
                break
    print(max(prev.iterkeys(), key=lambda k: prev[k]))

def test():
    

pb14()
