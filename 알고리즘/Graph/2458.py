N, M = map(int, input().split())
adj = [[0 for i in range(N)] for j in range(N)]

for i in range(M):
    p, c = map(int, input().split())
    adj[p-1][c-1] =1
for i in range(N):
    for row in range(N):
        for col in range(N):
            if adj[row][i] +adj[i][col]  ==2:
                adj[row][col] =1

cnt =[0 for i in range(N)]
for i in range(N):
    for j in range(N):
        if adj[i][j] ==1:
            cnt[i] +=1
            cnt[j] +=1

print(cnt.count(N-1))