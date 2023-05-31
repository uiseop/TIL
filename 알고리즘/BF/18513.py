from collections import deque


n,k = map(int,input().split())

sams = set(map(int, input().split()))

q = deque()

cnt = 0
answer = 0
visited = sams.copy()

def checkLeftRightHome(idx, weight=0):
  global answer, cnt

  for nid in [idx-1, idx+1]:
    if nid not in visited:
      q.append([nid, weight + 1])
      cnt += 1
      answer += weight + 1
      visited.add(nid)
      if cnt == k:
        print(answer)
        exit()

for sam in sams:
  checkLeftRightHome(sam)

while q:
  idx, weight = q.popleft()
  checkLeftRightHome(idx, weight)


