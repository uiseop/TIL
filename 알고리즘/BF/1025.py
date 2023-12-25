from itertools import combinations_with_replacement


N,M = map(int,input().split())

nums = set()

for i in range(10**5):
  nums.add(i**2)

po = list(list(input()) for _ in range(N))

c_diffs = [list([i]*M) for i in range(M)]

for d in range(1, M):
  for s in range(M):
    diff = []
    for i in range(s, M, d):
      diff.append(i)
    c_diffs.append(diff)

r_diffs = [list([i]*N) for i in range(N)]

for d in range(1, N):
  for s in range(N):
    diff = []
    for i in range(s, N, d):
      diff.append(i)
    r_diffs.append(diff)


answer = 0

for r in r_diffs:
  for c in c_diffs:
    # 더 많은 경우의 수가 있을 수 있음.
    num1 = ''
    for i in range(min(len(r), len(c))):
      row = r[i]
      col = c[i]
      num1 += po[row][col]
    num2 = ''
    for i in range(min(len(r), len(c))):
      row = r[i]
      col = c[len(r)-i-1]
      num2 += po[row][col]
    num3 = ''
    for i in range(min(len(r), len(c))):
      row = r[len(r)-i-1]
      col = c[i]
      num3 += po[row][col]
    num4 = ''
    for i in range(min(len(r), len(c))-1, -1, -1):
      row = r[i]
      col = c[i]
      num4 += po[row][col]
    
    possibles = []
    if int(num1) in nums:
      possibles.append(int(num1))
    if int(num2) in nums:
      possibles.append(int(num2))
    if int(num3) in nums:
      possibles.append(int(num3))
    if int(num4) in nums:
      possibles.append(int(num4))
    
    if possibles:
      answer = max(answer, max(possibles))



print(answer, r_diffs, c_diffs)

r_nums = [i for i in range(N)]
c_nums = [i for i in range(M)]

answer = ''

for i in range(1, min(N, M)):
  c_combis = combinations_with_replacement