import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())

maze = []

for _ in range(n):
    maze.append(list(input().rstrip()))

dr = [1,-1,0,0]
dc = [0,0,-1,1]

visited = [[False for _ in range(n)] for _ in range(n)]

def backTracking(row,col,count):
    if row == n-1 and col == n-1:
        return
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if maze[nr][nc] == "1": # 방문한곳이 흰 방이면!
                # case 1: 아직 미 방문
                # case 2: 이전에 방문했음 -> count 비교해서 진행할지 말지 결정
                if not visited[nr][nc] or visited[nr][nc] > count: 
                    visited[nr][nc] = count
                    backTracking(nr,nc,count)
            else: # 방문한곳이 검은방이네!
                # case 1: 아직 미 방문
                # case 2: 이전에 방문 -> count 비교
                if not visited[nr][nc] or visited[nr][nc] > count + 1:
                    visited[nr][nc] = count + 1
                    backTracking(nr,nc,count+1)

visited[0][0] = 1
backTracking(0,0,1)

print(visited[n-1][n-1] - 1)