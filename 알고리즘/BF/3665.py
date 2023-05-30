from collections import defaultdict, deque

T = int(input())

for _ in range(T):
  n = int(input())

  ranks = list(map(int,input().split()))
  edges = defaultdict(list)
  cntLinks = [-1] + [0 for _ in range(n)]

  for i in range(n):
    num = ranks[i]
    edges[num] = ranks[i+1:]
    cntLinks[num] = i
  
  m = int(input())
  for _ in range(m):
    a,b = map(int,input().split())

    if b in edges[a]:
      edges[a].remove(b)
      edges[b].append(a)
      cntLinks[a] += 1
      cntLinks[b] -= 1
    else:
      edges[b].remove(a)
      edges[a].append(b)
      cntLinks[a] -= 1
      cntLinks[b] += 1
  
  q = deque()
  
  for i in range(1, n+1):
    if not cntLinks[i]:
      q.append(i)
  if not q:
    print("IMPOSSIBLE")
    continue

  answer = []
  while q:
    node = q.popleft()
    answer.append(node)
    for i in edges[node]:
      if cntLinks[i]:
        cntLinks[i] -= 1
        if not cntLinks[i]:
          q.append(i)
  
  if len(answer) == n:
    print(*answer)
  else:
    print("IMPOSSIBLE")