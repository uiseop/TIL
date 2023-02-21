import sys

input = sys.stdin.readline

dir = [[-1,1], [-1,0], [-1,-1], [0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1]]

fish = []
dirs = []

answer = 0

for _ in range(4):
    inList = list(map(int,input().split()))
    f_lst = []
    d_lst = []
    for i in range(0, len(inList), 2):
        f_lst.append(inList[i])
        d_lst.append(inList[i+1])
    fish.append(f_lst)
    dirs.append(d_lst)

shark = [dirs[0][0], 0,0]
answer += fish[0][0]
fish[0][0] = 17

def getFishOrder():
    heap = [None for _ in range(17)]
    for r in range(4):
        for c in range(4):
            if fish[r][c] == 17 or fish[r][c] == 0: continue
            heap[fish[r][c]] = [r,c]
    return heap

def isPossible(r,c, d):
    for i in range(8):
        d = (d+i) % 8    
        dr, dc = dir[d]
        nr = r + dr
        nc = c + dc
        if 0 <= nr < 4 and 0 <= nc < 4 and fish[nr][nc] != 17:
            return [True, d]
    return [False, (d+1)%8]

def moveFish():
    heap = getFishOrder()
    for i in range(1,17):
        if not heap[i]: continue
        r,c = heap[i]
        res, d = isPossible(r,c,dirs[r][c])
        if res:
            dirs[r][c] = d
            nr = r + dir[d][0]
            nc = c + dir[d][1]
            if fish[nr][nc]:
                m_fish = fish[nr][nc]
                heap[m_fish] = [r,c]
            # 물고기 이동
            fish[r][c], fish[nr][nc] = fish[nr][nc], fish[r][c]
            dirs[r][c], dirs[nr][nc] = dirs[nr][nc], dirs[r][c] 
            


def backTracking(tot):
    global answer,shark
    answer = max(tot, answer)
    moveFish()
    for i in fish:
        print(i)
    print(tot, ';===================')
    for i in range(1,5):
        d,r,c = shark
        nr = r + dir[d][0] * i
        nc = c + dir[d][1] * i
        if 0 <= nr < 4 and 0 <= nc < 4 and fish[nr][nc] != 0:
            temp = fish[nr][nc]
            shark = [dirs[nr][nc], nr, nc]
            fish[nr][nc] = 17
            fish[r][c] = 0
            dirs[r][c] = None
            backTracking(tot + temp)
            fish[nr][nc] = temp
            fish[r][c] = 17
            dirs[r][c] = d
            shark = [dirs[r][c], r,c]

backTracking(answer)
print(answer)