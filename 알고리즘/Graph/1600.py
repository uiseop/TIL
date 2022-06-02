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

visited = [[False] * w for _ in range(h)]
visited[0][0] = True

answer = float("inf")

def dfs(r,c,horse,count):
    global answer
    if r == h-1 and c == w-1:
        answer = min(answer, count)
        return
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and pan[nr][nc] == 0:
            visited[nr][nc] = True
            dfs(nr,nc,horse,count + 1)
            visited[nr][nc] = False
    
    if horse < k:
        for i in range(8):
            nr = r + hr[i]
            nc = c + hc[i]
            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and pan[nr][nc] == 0:
                visited[nr][nc] = True
                dfs(nr,nc,horse + 1,count + 1)
                visited[nr][nc] = False

dfs(0,0,0,0)
print(answer)

# DFS는 방문 체크를 하지 않기 때문에 시간 복잡도는 지수 형태가 된다.
# BFS는 방문 체크를 해 줌으로써 선형 시간 복잡도를 갖는다. 때문에 최단 경로는 무조건 BFS 혹은 다익스트라로 푸는것이 맞다고 한다. 