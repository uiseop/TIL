import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    visited = [-1] * (n+1)
    visited[start] = 0
    q = deque()
    q.append(start)
    _max = [0,0]

    while q:
        frm = q.popleft()
        for to,weight in tree[frm]:
            if visited[to] == -1:
                visited[to] = visited[frm] + weight
                q.append(to)
                if _max[1] < visited[to]:
                    _max = to, visited[to]
    return _max

n = int(input())
if n == 1:
    print(0)
    exit()
tree = [[] for _ in range(n+1)]

for _ in range(n):
    opts = list(map(int,input().split()))
    frm = opts[0]
    for i in range(1, len(opts)-2, 2):
        tree[frm].append([opts[i], opts[i+1]])

node,dis = bfs(1)
node, dis = bfs(node)
print(dis)
# for t in tree:
#     print(t)
# []
# [[3, 2]]
# [[4, 4]]
# [[1, 2], [4, 3]]
# [[2, 4], [3, 3], [5, 6]]
# [[4, 6]]