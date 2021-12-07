def getPowerSet(n,k):
    if n == k:
        return [[k]]
    res = [[k]]

    temp = []
    for i in range(k+1, n+1):
        temp += getPowerSet(n,i)
    
    for i in range(len(temp)):
        temp[i] = [k] + temp[i]
    
    return res + temp

def powerSet(n):

    res = []
    for i in range(1,n+1):
        res += getPowerSet(n,i)
    
    return res

N = int(input())

result = powerSet(N)

for line in result:
    print(line)