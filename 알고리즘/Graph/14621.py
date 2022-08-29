import heapq
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

gender = [0] + list(input().split())

heap = []

parents = [i for i in range(n+1)]

for _ in range(m):
    v1,v2,d = map(int,input().split())
    if gender[v1] == gender[v2]:
        continue
    heapq.heappush(heap, [d, v1, v2])

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def find(a):
    if a == parents[a]:
        return a
    root = find(parents[a])
    parents[a] = root
    return root

ans = 0
cnt = 0

while heap:
    d, v1, v2 = heapq.heappop(heap)
    if find(v1) != find(v2):
        ans += d
        cnt += 1
        union(v1,v2)

print(ans) if cnt == n-1 else print(-1)