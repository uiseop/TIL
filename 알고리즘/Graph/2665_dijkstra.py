import heapq
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())

maze = []

for _ in range(n):
    maze.append(list(input().rstrip()))

visited = [[False for _ in range(n)] for _ in range(n)]

dr = [1,-1,0,0]
dc = [0,0,-1,1]

visited[0][0] = 1

heap = [[1,0,0]]

while heap:
    count, row, col = heapq.heappop(heap)
    if row == n-1 and col == n-1:
        break
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            if maze[nr][nc] == "1": # 흰 방이면!
                heapq.heappush(heap,[count,nr,nc])
                visited[nr][nc] = count
            else:
                heapq.heappush(heap,[count+1,nr,nc])
                visited[nr][nc] = count + 1

print(visited[n-1][n-1] - 1)
            
