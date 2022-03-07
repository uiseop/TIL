import sys

input = sys.stdin.readline

def isPossible(a, b):
    x1, y1, r1 = a
    x2, y2, r2 = b
    return (x1 - x2)**2 + (y1 - y2)**2 <= (r1 + r2)**2

def dfs(cur):
    for i in range(n):
        if visited[i] or cur == i or not isPossible(camps[cur], camps[i]):
            continue
        visited[i] = True
        dfs(i)

for _ in range(int(input())):
    n = int(input())
    camps = []
    for _ in range(n):
        camps.append(list(map(int,input().split())))
    visited = [False] * n
    ans = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            ans += 1
    print(ans)

# union find 방식으로 푼 풀이 -> 시간복잡도 훨씬 유리

def union(parent, x, y): # 더 작은 요소를 부모로 합침
    x = find(parent, x)
    y = find(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def find(parent, z):
    if z != parent[z]:
        parent[z] = find(parent, parent[z])
    # return parent[z]
    return z # parent[z] 를 하던 z를 하던 같음. root니까


def solution():
    ans = n
    parent = [i for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if (x_pos[i] - x_pos[j]) ** 2 + (y_pos[i] - y_pos[j]) ** 2 <= (radius[i] + radius[j]) ** 2:
                if find(parent, i) != find(parent, j):
                    union(parent, i, j)
                    ans -= 1

    return ans


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    x_pos, y_pos, radius = [], [], []
    for _ in range(n):
        x, y, r = map(int, sys.stdin.readline().split())
        x_pos.append(x)
        y_pos.append(y)
        radius.append(r)

    print(solution())