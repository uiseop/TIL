from collections import deque
import sys

input = sys.stdin.readline

w,h = map(int,input().split())

blocks = [[0 for _ in range(w + 2)]]

house = deque()
white = deque()

for H in range(1,h+1):
    inline = [0] + list(map(int,input().split())) + [0]
    blocks.append(inline)
    for i in range(1, w+2):
        if inline[i] == 1:
            house.append([H, i])


blocks.append([0 for _ in range(w + 2)])

answer = 0

odds = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (0,-1)]
evens = [(-1,-1), (-1,0), (0,1), (1,0), (1,-1), (0,-1)]

# outsider = [[0,0]]
visited = [[False for _ in range(w+2)] for _ in range(h+2)]
visited[0][0] = True
white.append([0,0])

while white:
    r,c = white.popleft()
    if r % 2 == 0:
        for dr,dc in evens:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < h+2 and 0 <= nc < w+2 and not visited[nr][nc] and blocks[nr][nc] == 0:
                visited[nr][nc] = True
                # outsider.append([nr,nc])
                white.append([nr,nc])
    else:
        for dr,dc in odds:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < h+2 and 0 <= nc < w+2 and not visited[nr][nc] and blocks[nr][nc] == 0:
                visited[nr][nc] = True
                # outsider.append([nr,nc])
                white.append([nr,nc])


while house:
    r,c = house.popleft()
    if r % 2 == 0:
        for dr, dc in evens:
            nr = r + dr
            nc = c + dc
            # if blocks[nr][nc] == 0 and [nr,nc] in outsider: ######### 시간복잡도 ⬆️ 1284ms
            if visited[nr][nc]: # 시간복잡도 ⬇️ 120ms
                # print(nr,nc, 'haha')
                answer += 1
    else:
        for dr, dc in odds:
            nr = r + dr
            nc = c + dc
            # if blocks[nr][nc] == 0 and [nr,nc] in outsider:
            if visited[nr][nc]:
                # print(nr,nc, 'haha')
                answer += 1


print(answer)
