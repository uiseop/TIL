import sys
sys.setrecursionlimit(10**6)
# 재귀 설정해주지 않으면 RecursionError 발생

def DFS(r,c):
    if r == n-1 and c == m-1:
        return 1
    if visited[r][c] != -1:
        return visited[r][c]
    visited[r][c] = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and jido[r][c] > jido[nr][nc]:
            visited[r][c] += DFS(nr,nc)

    return visited[r][c]

n,m = map(int,input().split())
jido = []
for _ in range(n):
    jido.append(list(map(int,input().split())))

visited = [[-1 for _ in range(m)] for _ in range(n)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

print(DFS(0,0))

# ✅ DFS와 DP의 조합으로 중복을 최소화해서 풀이. Top-Down방식으로 진행함.
# Visited배열을 -1로 초기화 했는데 이는 Top-down방식응로 진행하기 위해서 0을 맞춰주기 위함임.
# Bottom-Up방식이였으면 0으로 설정함.