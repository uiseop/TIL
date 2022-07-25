from collections import deque

s = int(input())
q = deque()
next_q = deque()
visited = [False] * 2001
q.append((1, 0))
time = 0

while True:
    if not q:
        time += 1
        q = next_q
        next_q = deque()
    now, clipboard = q.popleft()
    visited[now] = True
    if s in [now + clipboard, now - 1]:
        print(time + 1)
        break
    if clipboard != 0 and (now + clipboard) < 2000:
        if not visited[now + clipboard]:
            next_q.append((now + clipboard, clipboard))
    if now != 0:
        next_q.append((now, now))
        if not visited[now - 1]:
            next_q.append((now - 1, clipboard))

# DP 풀이

import sys

input = sys.stdin.readline

n = int(input())
dp = [i for i in range(1003)]
dp[1] = 0

for i in range(2, n+1):
    j = 2
    while i*j<20: 
        dp[i*j] = min(dp[i*j], dp[i]+j)
        dp[i*j-1] = min(dp[i*j]+1, dp[i*j-1])
        j+=1

print(dp[n])
