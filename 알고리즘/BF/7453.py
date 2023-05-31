from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())

A = []
B = []
C = []
D = []

for _ in range(n):
  a,b,c,d = list(map(int,input().split()))
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)

hap = {}
answer = 0

for a in A:
  for b in B:
    result = -1 * (a + b)
    if result in hap:
      hap[result] += 1
    else:
      hap[result] = 1

for c in C:
  for d in D:
    result = c + d
    if result in hap:
      answer += hap[result]

print(answer)