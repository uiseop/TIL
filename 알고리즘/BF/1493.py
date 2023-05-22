import math
import sys

input = sys.stdin.readline

L,W,H = map(int,input().split())
n = int(input())

counts = []

for _ in range(n):
  _,count = map(int,input().split())
  counts.append(count)

def func(l,w,h):
  result = 0

  if not l or not w or not h:
    return result
  
  k = min(l,w,h)
  t = math.log2(k)

  while t >= 0:
    if not counts[t]: continue

    counts[t] -= 1
    T = math.pow(2, t)

    result += func(l-T, T, h) + func(l, w-T, h) + func(T, T, h-T) + 1
    t -= 1

  return result

answer = func(L,W,H)

