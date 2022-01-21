def addDecrease(digit, num):
    if digit == 1:
        decrease.append(num)
    else:
        for i in range(num % 10):
            addDecrease(digit-1, num*10 + i)


n = int(input())

decrease = []

for i in range(1, 11):
    for j in range(0,10):
        addDecrease(i,j)

if n > len(decrease) - 1:
    print(-1)
else:
    print(decrease[n])