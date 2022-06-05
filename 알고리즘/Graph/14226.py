from collections import deque
n = int(input())
dist = [[-1]* (2*n+1) for _ in range(2*n+1)]
q = deque()
q.append((1,0))  # 화면 이모티콘 개수, 클립보드 이모티콘 개수
dist[1][0] = 0
while q:
    s,c = q.popleft()
    if s == n:
        print(dist[s][c])
        break
    if dist[s][s] == -1: # 방문하지 않았으면
        dist[s][s] = dist[s][c] + 1
        q.append((s,s))
    if s+c <= n and dist[s+c][c] == -1:
        dist[s+c][c] = dist[s][c] + 1
        q.append((s+c, c))
    if s-1 >= 0 and dist[s-1][c] == -1:
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1, c))

# answer = -1
# for i in range(n+1):
#     if dist[n][i] != -1:
#         if answer == -1 or answer > dist[n][i]:
#             answer = dist[n][i]
# print(answer)

from collections import deque 

def bfs(target):
    queue = deque([(1,0,0)])
    visited = [False for i in range(target*2+1)]
    stacked = [False for i in range(target*2+1)]
    while True :
        value, clip, time = queue.popleft()
        visited[value] = True
        if value == target:
            return time 
        else:
            if value+clip<target*2 and not visited[value+clip] :
                queue.append((value+clip, clip, time+1))
            if not stacked[value]:
                queue.append((value, value, time+1))
                stacked[value] =True
            if value>1 and not visited[value-1]:
                queue.append((value-1, clip, time+1))

N = int(input())
print(bfs(N))
