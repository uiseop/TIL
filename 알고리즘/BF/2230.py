from bisect import bisect_left


N,M = map(int,input().split())

A = list(int(input()) for _ in range(N))

A.sort()

result = float("INF")

for a in A:
  num = a + M
  idx = bisect_left(A, num)
  if idx == len(A):
    break
  
  result = min(result, A[idx] - a)

print(result)
