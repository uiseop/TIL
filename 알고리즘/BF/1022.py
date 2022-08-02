import sys

input = sys.stdin.readline

r1,c1,r2,c2 = map(int,input().split())

board = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]

n = (c2-c1+1) * (r2-c1+1)

dr = [0,-1,0,1] # 우, 상, 좌, 하
dc = [1,0,-1,0]

row = 0
col = 0
num = 1
dir = 0
cnt = 0
dcnt = 1

while n > 0:
    if r1 <= row <= r2 and c1 <= col <= c2:
        n -= 1
        board[row-r1][col-c1] = num
        max_num = num
    num += 1
    cnt += 1
    row += dr[dir]
    col += dc[dir]

    if cnt == dcnt:
        cnt = 0
        dir = (dir+1) % 4
        if dir == 0 or dir == 2:
            dcnt += 1

max_num_len = len(str(max_num))
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(board[i][j]).rjust(max_num_len), end=' ')
    print()