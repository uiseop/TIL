import sys
from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def BFS(row,col):
    dq = deque()
    dq.append([row,col])
    blocks[row][col] = 1
    while dq:
        r,c = dq.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and blocks[nr][nc] == "0":
                blocks[r][c] = 1
                dq.append([nr,nc])
                history.append([nr,nc])

def count(row,col):
    set_cnt = set()
    tot = 1
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr < n and 0 <= nc < m and type(blocks[nr][nc]) != str:
            set_cnt.add(tuple(blocks[nr][nc]))
    for cnt,r,c in set_cnt:
        tot += cnt
    return tot

input = sys.stdin.readline

n,m = map(int,input().split())
blocks = list(list(input().rstrip()) for _ in range(n))

for row in range(n):
    for col in range(m):
        history = []
        if blocks[row][col] == "0":
            history.append([row,col])
            BFS(row,col)
            length = len(history)
            print(history, length)
            for r,c in history:
                blocks[r][c] = [length, row,col]

for i in blocks:
    print(i)
ans = [["0" for _ in range(m)] for _ in range(n)]
for row in range(n):
    for col in range(m):
        if blocks[row][col] == "1":
            ans[row][col] = str(count(row,col) % 10)

print("\n\n\n")
for i in ans:
    print(''.join(i))