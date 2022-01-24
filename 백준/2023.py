import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def DFS(nums, cnt):
    if cnt == n:
        pri.append(''.join(map(str,nums)))
        return
    for i in range(10):
        nums.append(i)
        num = int(''.join(map(str, nums)))
        if isPrime(num):
            DFS(nums, cnt + 1)
        nums.pop()
    

n = int(input())

pri = []

for i in range(2,10):
    if isPrime(i):
        DFS([i], 1)

for i in pri:
    print(i)
