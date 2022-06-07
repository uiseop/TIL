from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
inDepth = [0 for _ in range(n+1)]
adj = [[] for _ in range(n+1)]
for _ in range(m):
    orders = list(map(int,input().split()))
    len_orders = orders[0]
    orders = orders[1:]
    for i in range(len(orders) - 1):
        adj[orders[i]].append(orders[i+1])
        inDepth[orders[i+1]] += 1

q = deque()

for i in range(1,n+1):
    if inDepth[i] == 0:
        q.append(i)

answer = []

while q:
    sing = q.popleft()
    answer.append(sing)
    for order in adj[sing]:
        inDepth[order] -= 1
        if inDepth[order] == 0:
            q.append(order)

if len(answer) == n:
    for sing in answer:
        print(sing)
else:
    print(0)