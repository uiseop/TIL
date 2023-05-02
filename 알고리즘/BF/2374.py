N = int(input())

A = list(int(input()) for _ in range(N))

parents = [i for i in range(N)]

def union(a,b):
  parentA = find(a)
  parentB = find(b)

  A[parentA] = max(A[parentA], A[parentB])
  A[parentB] = max(A[parentA], A[parentB])

  if parentA <= parentB:
    parents[parentB] = parentA
  else:
    parents[parentA] = parentB

def find(a):
  if a == parents[a]:
    return parents[a]
  
  parentA = find(parents[a])
  parents[a] = parentA
  return parentA

pre = A[0]
for i in range(1, N):
  if A[i] == pre:
    if find(i-1) != find(i):
      union(i-1, i)
  pre = A[i]

heap = []

def findRoots():
  roots = [0]
  pre = 0
  for i in range(1,N):
    if find(pre) != find(i):
      roots.append(i)
      pre = i
  return roots

roots = findRoots()

def findMinDiff(roots):
  minDiff = float("INF")
  idx = 0
  for i in range(len(roots)-1):
    if abs(A[roots[i]] - A[roots[i+1]]) < minDiff:
      minDiff = abs(A[roots[i]] - A[roots[i+1]])
      idx = i
  
  union(roots[idx], roots[idx+1])
  return minDiff

answer = 0

while len(roots) > 1:
  answer += findMinDiff(roots)

  roots = findRoots()

print(answer)


0 10 1 6 6 7

      



