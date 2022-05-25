from collections import deque
import sys
input = sys.stdin.readline

# m이 가로고, n이 세로임. 주의하셈
m,n = map(int, input().split()) 

dr = [1,-1,0,0]
dc = [0,0,1,-1]

room = list(list(map(int, input().rstrip())) for _ in range(n))

dq = deque()
visited = [[False for _ in range(m)] for _ in range(n)]

visited[0][0] = True
dq.append([0,0,0])
answer = 0
while dq:
    r,c,cnt = dq.popleft()
    if (r == n-1 and c == m-1):
        answer = cnt
        break
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if (0 <= nr < n and 0 <= nc < m and not visited[nr][nc]):
            visited[nr][nc] = True
            if room[nr][nc]:
                dq.append([nr,nc,cnt+1])
            else:
                dq.appendleft([nr,nc,cnt])

print(answer)