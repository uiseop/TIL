import sys

input = sys.stdin.readline

memo = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
for i in range(21):
    for j in range(21):
        memo[0][i][j] = 1
        memo[i][0][j] = 1
        memo[i][j][0] = 1

for i in range(1,21):
    for j in range(1,21):
        for k in range(1,21):
            if (i < j and j < k):
                memo[i][j][k] = memo[i][j][k-1] + memo[i][j-1][k-1] - memo[i][j-1][k]
            else:
                memo[i][j][k] = memo[i-1][j][k] + memo[i-1][j-1][k] + memo[i-1][j][k-1] - memo[i-1][j-1][k-1]

a,b,c = map(int,input().split())
while (a != -1 or b != -1 or c != -1):
    if ( a <= 0 or b <= 0 or c <= 0):
        print("w(%d, %d, %d) ="%(a,b,c),1)
    elif (a > 20 or b > 20 or c > 20):
        print("w(%d, %d, %d) ="%(a,b,c),memo[20][20][20])
    else:
        print("w(%d, %d, %d) ="%(a,b,c),memo[a][b][c])
    a,b,c = map(int,input().split())