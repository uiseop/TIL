# 🤔 메모리 초과
# for _ in range(int(input())):
#     v,e = map(int,input().split())
#     graph = [[0 for _ in range(v+1)] for _ in range(v+1)]
#     for _ in range(e):
#         frm,to = map(int,input().split())
#         graph[frm][to] = 1
#         graph[to][frm] = 1
#         if sum(graph[frm]) > 2 or sum(graph[to]) > 2:
#             print("NO")
#             break
#     else:
#         print("YES")
import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline
# ⬆️위에 2개 안쓰면 시간초과 뜸. 입력이 길어서 그런가봄.

def dfs(v, mark):
    visited[v] = mark
    for node in graph[v]:
        if visited[node] == 0:
            dfs(node, -mark)

for _ in range(int(input())):
    v,e = map(int,input().split())
    visited = [0 for _ in range(v+1)]
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        frm, to = map(int,input().split())
        graph[frm].append(to)
        graph[to].append(frm)
    
    for i in range(1,v+1):
        if visited[i] == 0:
            dfs(i, 1)

    flag = True
    for i in range(1, v+1):
        for j in graph[i]:
            if visited[i] != -visited[j]:
                flag = False
    print("YES") if flag else print("NO")
