from collections import defaultdict, deque

N,T = map(int,input().split())

pos = set()

for _ in range(N):
  r,c = map(int,input().split())
  pos.add((r,c))

answer = -1

q = deque()
q.append([0,0,0])

while q:
  r,c,count = q.popleft()

  if c == T:
    answer = count
    break

  for i in range(-2, 3):
    for j in range(-2, 3):
      nr,nc = r + i, c + j
      if (nr,nc) in pos:
        q.append([nr,nc,count + 1])
        pos.remove((nr,nc))

print(answer)