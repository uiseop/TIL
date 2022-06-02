from collections import deque
import sys

input = sys.stdin.readline

k = int(input())
w,h = map(int,input().split())
pan = list(list(map(int, input().split())) for _ in range(h))

hr = [-2,-1,1,2,2,1,-1,-2]
hc = [1,2,2,1,-1,-2,-2,-1]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

visited = [[[0 for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]
q = deque()
q.append([0,0,0])
flag = False

while q:
    r,c,K = q.popleft()
    if r == h-1 and c == w-1:
        flag = True
        print(max(visited[r][c]))
        break
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr == 0 and nc == 0: continue
        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc][K] and pan[nr][nc] == 0:
            visited[nr][nc][K] = visited[r][c][K] + 1
            q.append([nr,nc,K])
    
    if K < k:
        for i in range(8):
            nr = r + hr[i]
            nc = c + hc[i]

            if nr == 0 and nc == 0: continue
            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc][K+1] and pan[nr][nc] == 0:
                visited[nr][nc][K+1] = visited[r][c][K] + 1
                q.append([nr,nc,K+1])

if not flag:
    print(-1)
# answer = float("inf")

# def dfs(r,c,horse,count):
#     global answer
#     if r == h-1 and c == w-1:
#         answer = min(answer, count)
#         return
    
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and pan[nr][nc] == 0:
#             visited[nr][nc] = True
#             dfs(nr,nc,horse,count + 1)
#             visited[nr][nc] = False
    
#     if horse < k:
#         for i in range(8):
#             nr = r + hr[i]
#             nc = c + hc[i]
#             if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and pan[nr][nc] == 0:
#                 visited[nr][nc] = True
#                 dfs(nr,nc,horse + 1,count + 1)
#                 visited[nr][nc] = False

# DFS는 방문 체크를 하지 않기 때문에 시간 복잡도는 지수 형태가 된다.
# BFS는 방문 체크를 해 줌으로써 선형 시간 복잡도를 갖는다. 때문에 최단 경로는 무조건 BFS 혹은 다익스트라로 푸는것이 맞다고 한다. 