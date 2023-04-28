import sys

input = sys.stdin.readline

n,m = map(int,input().split())

T = []

for _ in range(n):
  T.append(int(input()))

left = 0
right = min(T) * m

answer = right

def getCount(time):
  cnt = 0
  for t in T:
    cnt += time // t
  return cnt

while True:
  if left <= right:
    middle = (left + right) // 2
    cnt = getCount(middle)
    if cnt >= m:
      right = middle - 1
      answer = middle
    else:
      left = middle + 1
  else:
    break

print(answer)