from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [{} for _ in range(n + 1)]

frm, to = map(int,input().split())

for _ in range(m):
    h1,h2,k = map(int,input().split())
    graph[h1][h2] = k
    graph[h2][h1] = k

def BFS(Limit):
    q = deque()
    visited = [False for _ in range(n+1)]
    q.append(frm)
    while q:
        node = q.popleft()
        if node == to: return True
        for next_node, weight in graph[node].items():
            if not visited[next_node] and weight >= Limit:
                visited[next_node] = True
                q.append(next_node)

    return False

left = 0
right = 1000000

while left <= right:
    mid = (left + right) // 2
    if BFS(mid):
        left = mid + 1
    else:
        right = mid - 1
    
if right == -1:
    print(0)
else:
    print(right)