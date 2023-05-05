import sys

input = sys.stdin.readline

n = int(input())

result = []
ms = list(int(input()) for _ in range(n))
stack = []
cur = 0

for m in ms:
  if cur < m:
    for k in range(cur + 1, m + 1):
      result.append('+')
      stack.append(k)
    result.append('-')
    stack.pop()
    cur = m
  else:
    num = stack.pop()
    if num == m:
      result.append('-')
    else:
      print('NO')
      exit()

for r in result:
  print(r)