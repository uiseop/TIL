import sys

input = sys.stdin.readline

n = int(input())

pos = [list(map(float, input().split())) for _ in range(n)]

dist = []

def cal_distance(pos1, pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    return round(((x1-x2)**2 + (y1-y2)**2) ** 0.5,2)

for i in range(n-1):
    for j in range(i+1, n):
        d = cal_distance(pos[i], pos[j])
        dist.append([d, i,j])

dist.sort()

parents = [i for i in range(n)]

def find(a):
    if a == parents[a]:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a,b):
    a = parents[a]
    b = parents[b]
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

answer = 0

for d,i,j in dist:
    if find(i) != find(j):
        union(i,j)
        answer += d

print(answer)
