from itertools import permutations
import sys

input = sys.stdin.readline

s = list(input().rstrip())

sets = set()

permutes = permutations(s)

answer = 0

def isRucky(arr):
  string = ''.join(arr)
  if string in sets:
    return False
  for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
      continue
    else:
      break
  else:
    sets.add(string)
    return True
  return False

for p in permutes:
  if isRucky(p):
    answer += 1

print(answer)
    