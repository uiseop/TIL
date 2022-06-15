import sys

input = sys.stdin.readline

INF = sys.maxsize

t = int(input())

def bf(start):
    dist = [INF for _ in range(n+1)]
    dist[start] = 0

    for i in range(1,n+1):
        update = False
        for j in range(1,n+1):
            for e,t in road[j]:
                if dist[e] > dist[j] + t:
                    dist[e] = dist[j] + t
                    update = True
                    if i == n:
                        return True
        if not update:
            return False


for _ in range(t):
    n,m,w = map(int,input().split())

    road = [[] for _ in range(n+1)]

    for _ in range(m):
        s,e,t = map(int,input().split())
        road[s].append([e,t])
        road[e].append([s,t])
    
    for _ in range(w):
        s,e,t = map(int,input().split())
        road[s].append([e,-t])
    
    
    if bf(1):
        print("YES")
    else:
        print("NO")