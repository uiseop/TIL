import sys

input = sys.stdin.readline

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def dfs(arr, idx):
    if idx == len(word):
        return 1
    r,c = arr
    if dp[r][c][idx] != -1:
        return dp[r][c][idx]
    
    dp[r][c][idx] = 0
    for i in range(4):
        for k in range(1,K+1):
            nr = r + (dr[i]*k)
            nc = c + (dc[i]*k)
            if 0 <= nr < N and 0 <= nc < M and pan[nr][nc] == word[idx]:
                dp[r][c][idx] += dfs([nr,nc], idx + 1)

    return dp[r][c][idx]

N,M,K = map(int,input().split())
pan = list(list(input().rstrip()) for _ in range(N))
word = list(input().rstrip())

ans = 0
dp = [[[-1 for _ in range(len(word))] for _ in range(M)] for _ in range(N)]
for row in range(N):
    for col in range(M):
        if pan[row][col] == word[0]:
            ans += dfs([row,col], 1)

print(ans)