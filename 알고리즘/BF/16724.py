from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

arr = list(list(input().rstrip()) for _ in range(n))

visited = dict()

def union(a,b):
    pA = find(a)
    pB = find(b)
    if pA < pB:
        parents[pB] = pA
    else:
        parents[pA] = pB

def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]

parents = [i for i in range(n*m)]

def dir(r,c):
    if arr[r][c] == 'U':
        return [r-1, c]
    elif arr[r][c] == 'D':
        return [r+1, c]
    elif arr[r][c] == 'L':
        return [r,c-1]
    else:
        return [r,c+1]

for r in range(n):
    for c in range(m):
        nr, nc = dir(r,c)
        nxt = nr * m + nc
        cur = r * m + c
        union(nxt, cur)

result = 0

for i in range(n*m):
    if find(i) not in visited:
        result += 1
        visited[i] = True

print(result)