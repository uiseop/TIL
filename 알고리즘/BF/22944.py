import heapq
import sys

input = sys.stdin.readline

N, H, D = map(int,input().split())

rect = [list(input().rstrip()) for _ in range(N)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]

start = [0,0]
end = [0,0]
flag = 0

for row in range(N):
    for col in range(N):
        if rect[row][col] == 'S':
            start = [row, col]
            flag += 1
        elif rect[row][col] == 'E':
            end = [row,col]
            flag += 1
        if flag == 2:
            break 
    if flag == 2:
        break

visited = [[0 for _ in range(N)] for _ in range(N)]
visited[start[0]][start[1]] = H

heap = []
heapq.heappush(heap, [0, start[0], start[1], H, 0])

def isInRange(r,c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False

def solve():
    while heap:
        step, r ,c ,h ,u = heapq.heappop(heap)
        
        if h == 0:
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if isInRange(nr,nc):
                if rect[nr][nc] == 'E':
                    return step

                if rect[nr][nc] == 'U':
                    if visited[nr][nc] < h:
                        visited[nr][nc] = h
                        heapq.heappush(heap, [step+1, nr,nc, h, D-1])
                elif u:
                    if visited[nr][nc] < h:
                        visited[nr][nc] = h
                        heapq.heappush(heap, [step+1, nr,nc, h, u-1])
                else:
                    if visited[nr][nc] < h-1:
                        visited[nr][nc] = h-1
                        heapq.heappush(heap, [step+1, nr, nc, h-1, 0])
    return False

result = solve()

if not result:
    print(-1)
else:
    print(result + 1)
