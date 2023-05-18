from collections import defaultdict


def solve(k,s):
  numCounts = {}
  visited = defaultdict(bool)

  for num in s:
    modNum = num % k
    if numCounts.get(modNum):
      numCounts[modNum] += 1
    else:
      numCounts[modNum] = 1
  
  result = 0
  for num, count in numCounts.items():
    print(num, count)
    if visited[num]: continue
    if num == 0:
      result += 1
      continue

    oppositeNum = k - num
    if num == oppositeNum:
      result += 1
    else:
      if numCounts.get(oppositeNum):
        result += max(count, numCounts[oppositeNum])
      else:
        result += count
      visited[num] = True
      visited[oppositeNum] = True
  
  print(result)
  
k = 7
inputs = '278 576 496 727 410 124 338 149 209 702 282 718 771 575 436'
s = list(map(int,inputs.split()))

print(solve(k,s))