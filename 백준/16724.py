import sys
input = sys.stdin.readline

def getRoot(x):
    if x == root[x]:
        return x
    root[x] = getRoot(root[x])
    return root[x]

def unionRoot(x,y):
    rx = getRoot(x)
    ry = getRoot(y)
    if rx == ry: # 두 개의 root가 같으면 끝
        return
    # 다르면 더 작은값을 root로
    if rx < ry: 
        root[ry] = rx
    else:
        root[rx] = ry

n,m = map(int,input().split())
zido = list(list(input().rstrip()) for _ in range(n))

d = {
    "D": [1,0],
    "L": [0,-1],
    "R": [0,1],
    "U": [-1,0]
}

root = [i for i in range(n*m)]

for r in range(n):
    for c in range(m):
        direction = d[zido[r][c]]
        nr = r + direction[0]
        nc = c + direction[1]
        cur = r*m + c
        nxt = nr*m + nc
        unionRoot(cur, nxt)

ans = 0
visited = dict()

for i in range(n*m):
    if getRoot(i) not in visited:
        ans += 1
        visited[root[i]] = True
print(ans)