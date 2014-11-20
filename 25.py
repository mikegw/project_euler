def brute():
    current = 1
    previous = 0
    i = 1
    while True:
        current, previous, i = current + previous, current, i+1
        if len(str(current)) == 1000:
            print(i,current)
            break

brute()
