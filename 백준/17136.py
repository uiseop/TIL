from operator import le
from textwrap import indent


def check(r,c, length):
    temp = 0
    for i in range(length):
        temp += sum(inData[r+i][c:c+length])
    if temp == length ** 2:
        return True
    return False

def DFS(o, cnt):
    global ans

    if o == 0:
        ans = min(ans, cnt)
        return
    if cnt > ans:
        return
    if sum(used) == 0:
        return
    
    for r in range(10):
        for c in range(10):
            if inData[r][c] == 1:
                for length in range(5,0,-1):
                    if used[length] and r + length <= 10 and c + length <= 10:
                        if check(r,c, length):
                            for i in range(r, r+length):
                                for j in range(c, c+length):
                                    inData[i][j] = 0
                            used[length] -= 1
                            DFS(o - length ** 2, cnt + 1)
                            for i in range(r, r+length):
                                for j in range(c, c+length):
                                    inData[i][j] = 1
                            used[length] += 1
                return

    


inData = [list(map(int,input().split())) for _ in range(10)]
used = [0] + [5]*5
ans = float("inf")
one = 0

for line in inData:
    one += sum(line)

if one == 0:
    print(0)
else:
    DFS(one, 0)
    print(-1) if ans == float("inf") else print(ans)

