from collections import defaultdict, deque
heap = []

N,M = map(int,input().split())

isImpossible = defaultdict(bool)

for _ in range(M):

  m = int(input())
  isImpossible[m] = True

answer = -1

q = deque()

visited = [False for _ in range(N+1)]

if not isImpossible[2]:
  q.append([1, 2, 1])

while q:
  count, cur, pre = q.popleft()

  if cur == N:
    answer = count

  for d in [1,0,-1]:
    jump = pre + d
    next = cur + jump
    if not jump or isImpossible[next] or next > N or visited[next]: continue
    visited[next] = True
    q.append([count + 1, next, jump])

print(answer)

