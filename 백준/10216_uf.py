import sys

input = sys.stdin.readline

def union(parent,x,y):
    x = find(parent, x)
    y = find(parent, y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

def find(parent, z):
    if z != parent[z]:
        parent[z] = find(parent, parent[z])
    return parent[z]

def solution():
    ans = n
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if (x_pos[i]-x_pos[j])**2 + (y_pos[i]-y_pos[j])**2 <= (r_pos[i]+r_pos[j])**2:
                if find(parent, i) != find(parent, j):
                    union(parent,i,j)
                    ans -= 1
    return ans


for _ in range(int(input())):
    n = int(input())
    x_pos = []
    y_pos = []
    r_pos = []
    for _ in range(n):
        x,y,r = map(int,input().split())
        x_pos.append(x)
        y_pos.append(y)
        r_pos.append(r)

    print(solution())