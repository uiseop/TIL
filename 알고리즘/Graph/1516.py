from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

inEdge = [0 for _ in range(n)]
next_bulid = [[] for _ in range(n)]
time = [0 for _ in range(n)]
answer_time = [0 for _ in range(n)]
temp_time = [[] for _ in range(n)]

for i in range(n):
    build_info = list(map(int,input().split()))
    time[i] = build_info[0]
    if len(build_info) == 2: continue
    for nb in build_info[1:-1]:
        next_bulid[nb-1].append(i)
        inEdge[i] += 1

q = deque()
for i in range(n):
    if inEdge[i] == 0:
        q.append(i)
        answer_time[i] = time[i]

# print(next_bulid)
# print(inEdge)

while q:
    build = q.popleft()
    for nb in next_bulid[build]:
        inEdge[nb] -= 1
        temp_time[nb].append(answer_time[build])
        # answer_time[nb] += answer_time[build]
        if inEdge[nb] == 0:
            answer_time[nb] += time[nb]
            answer_time[nb] += max(temp_time[nb])
            q.append(nb)

for ans in answer_time:
    print(ans)

