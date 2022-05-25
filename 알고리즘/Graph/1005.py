from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n,k = map(int,input().split())
    time = [0] + list(map(int,input().split()))
    tree = [[] for _ in range(n+1)]
    inDegree = [0 for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    for _ in range(k):
        d1,d2 = map(int, input().split())
        tree[d1].append(d2)
        inDegree[d2] += 1
    
    q = deque()
    for i in range(1,n+1):
        if inDegree[i] == 0:
            q.append(i)
            dp[i] = time[i]
    
    while q:
        a = q.popleft()
        for i in tree[a]:
            inDegree[i] -= 1
            dp[i] = max(dp[a] + time[i], dp[i])
            if inDegree[i] == 0:
                q.append(i)

    w = int(input())
    print(dp[w])