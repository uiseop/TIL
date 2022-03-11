import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(str,input().split())
    zeroN = 0
    zeroM = 0
    diff = 0
    for i in range(len(n)):
        if n[i] == m[i]:
            continue
        diff += 1
        if n[i] == "0":
            zeroN += 1
        elif m[i] == "0":
            zeroM += 1
    diffZero = abs(zeroN - zeroM)
    ans = (diff - diffZero) // 2 + diffZero
    print(ans)