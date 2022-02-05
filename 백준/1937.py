import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dr = [1,-1,0,0]
dc = [0,0,-1,1]

def dfs(r,c):
    if DP[r][c]:
        return DP[r][c]

    DP[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and boo[nr][nc] > boo[r][c]:
            DP[r][c] = max(DP[r][c], dfs(nr,nc) + 1)

    return DP[r][c]

n = int(input())
boo = []
for _ in range(n):
    boo.append(list(map(int,input().split())))

DP = [[0 for _ in range(n)] for _ in range(n)]
ans = 0
for r in range(n):
    for c in range(n):
        ans = max(ans, dfs(r,c)) 

print(ans)

# ✅DFS 탐색에서 이미 탐색한 곳을 재탐색하는것을 방지하기 위한 DFS + DP의 조합으로 풀이를 진행하면
# 시간복잡도를 크게 줄일 수 있음
# 대나무 숲의 각 좌표 (i, j)에 대해서 앞으로 이동할 수 있는 최장 경로의 길이는 재차 계산할 필요가 없습니다. 
# 한 번 계산했다면 그걸 재활용하는 방식, 즉, DP를 생각해볼 수 있겠네요.