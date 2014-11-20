days_in_month = {0:31,1:28,2:31,3:30,4:31,5:30,6:31,7:31,8:30,9:31,10:30,11:31}

day = [1,0,0,1901]
count = 0

while day[3] < 2001:
    if day[0] == 6 and day[1] == 0:
        count += 1

    if day[3] % 4 == 0:
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28

    day = [(day[0]+1) % 7, day[1]+1, day[2],day[3]]
    if day[1] == days_in_month[day[2]]:
        day[1] = 0
        day[2] += 1
        if day[2] == 12:
            day[2] = 0
            day[3] += 1
        

print(count)
