from collections import deque

def bfs(x, y):
    q.append(x)
    c[x] = 0
    while q:
        nx = q.popleft()
    for i in a[nx]:
        if c[i] == -1:
            q.append(i)
            c[i] = c[nx] + 1

n = int(input())
start, end = map(int, input().split())
m = int(input())
a = [[] for _ in range(n)]
c = [-1 for _ in range(n)]
q = deque()

for i in range(m):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    a[x].append(y)
    a[y].append(x)

bfs(start-1, end-1)
if c[end-1] == -1:
    print(-1)
else:
    print(c[end-1]//2)