#for i in range(1,11):
    #print(i,i*(9**5))

def sum_digits5(n):
    x = 0
    for i in str(n):
        x += int(i)**5
    return x
def pb30():
    ans = 0
    for i in range(10,6*(9**5)):
        if sum_digits5(i) == i:
            print(i)
            ans += i
    print(ans)

pb30()
