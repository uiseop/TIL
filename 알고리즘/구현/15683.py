import sys

input = sys.stdin.readline

# 한번에 1개씩            
row1 = [1,-1,0,0]
col1 = [0,0,1,-1]
# 한번에 2개씩
row2 = [[1,-1],[0,0]]
col2 = [[0,0],[1,-1]]
# 한번에 2개씩
row3 = [[-1,0],[1,0],[1,0],[-1,0]]
col3 = [[0,1],[0,1],[0,-1],[0,-1]]
# 한번에 3개씩
row4 = [[-1,0,0],[1,-1,0],[1,0,0],[-1,1,0]]
col4 = [[0,-1,1],[0,0,1],[0,-1,1],[0,0,-1]]

def dfs(cid):
    global answer
    if cid == len(cctv):
        cnt = 0
        for ch in check:
            cnt += ch.count(False)
        answer = min(answer, cnt)
        return 
    r,c,num = cctv[cid]
    if num == 1:
        for i in range(4):
            dr = r + row1[i]
            dc = c + col1[i]
            changed = []
            while 0 <= dr < n and 0 <= dc < m and room[dr][dc] != 6:
                if room[dr][dc] != 0 or check[dr][dc] == True:
                    dr += row1[i]
                    dc += col1[i]
                    continue
                changed.append([dr,dc])
                check[dr][dc] = True
                dr += row1[i]
                dc += col1[i]
            dfs(cid+1)
            for row,col in changed:
                check[row][col] = False
                
    elif num == 2:
        for i in range(2):
            changed = []
            for j in range(2):
                dr = r + row2[i][j]
                dc = c + col2[i][j]
                
                while 0 <= dr < n and 0 <= dc < m and room[dr][dc] != 6:
                    if room[dr][dc] != 0 or check[dr][dc] == True:
                        dr += row2[i][j]
                        dc += col2[i][j]
                        continue
                    changed.append([dr,dc])
                    check[dr][dc] = True
                    dr += row2[i][j]
                    dc += col2[i][j]
            dfs(cid+1)
            for row,col in changed:
                check[row][col] = False

    elif num == 3:
        for i in range(4):
            changed = []
            for j in range(2):
                dr = r + row3[i][j]
                dc = c + col3[i][j]
                while 0 <= dr < n and 0 <= dc < m and room[dr][dc] != 6:
                    if room[dr][dc] != 0 or check[dr][dc] == True:
                        dr += row3[i][j]
                        dc += col3[i][j]
                        continue
                    changed.append([dr,dc])
                    check[dr][dc] = True
                    dr += row3[i][j]
                    dc += col3[i][j]
            dfs(cid+1)
            for row,col in changed:
                check[row][col] = False
    elif num == 4:
        for i in range(4):
            changed = []
            for j in range(3):
                dr = r + row4[i][j]
                dc = c + col4[i][j]
                while 0 <= dr < n and 0 <= dc < m and room[dr][dc] != 6:
                    if room[dr][dc] != 0 or check[dr][dc] == True:
                        dr += row4[i][j]
                        dc += col4[i][j]
                        continue
                    changed.append([dr,dc])
                    check[dr][dc] = True
                    dr += row4[i][j]
                    dc += col4[i][j]
            dfs(cid+1)
            for row,col in changed:
                check[row][col] = False
    else:
        changed = []
        for i in range(4):
            dr = r + row1[i]
            dc = c + col1[i]
            while 0 <= dr < n and 0 <= dc < m and room[dr][dc] != 6:
                if room[dr][dc] != 0 or check[dr][dc] == True:
                    dr += row1[i]
                    dc += col1[i]
                    continue
                changed.append([dr,dc])
                check[dr][dc] = True
                dr += row1[i]
                dc += col1[i]
        dfs(cid+1)
        for row,col in changed:
            check[row][col] = False

answer = float('inf')
n,m = map(int,input().split())
room = []
cctv = []
check = [[False]*m for _ in range(n)]
for row in range(n):
    place = list(map(int,input().split()))
    room.append(place)
    for i in range(len(place)):
        if place[i] in [1,2,3,4,5]:
            check[row][i] = True
            cctv.append([row,i,place[i]])
            
        elif place[i] == 6:
            check[row][i] = True

dfs(0)
print(answer)