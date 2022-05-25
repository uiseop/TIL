from collections import deque
import sys
input = sys.stdin.readline

v,e = map(int,input().split())
parent = [i for i in range(v+1)]
edges = []
answer = 0
for _ in range(e):
    edges.append(list(map(int,input().split())))

edges.sort(key=lambda x: x[2])

def find(x):
    if x == parent[x]:
        return x
    p = find(parent[x])
    parent[x] = p
    return p

for a,b,c in edges:
    pa = find(a)
    pb = find(b)
    if (pa != pb):
        if pa > pb:
            parent[pa] = pb
        else:
            parent[pb] = pa
        answer += c

print(answer)