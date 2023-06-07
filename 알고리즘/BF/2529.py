k = int(input())

A = list(input().split())
visited = [False for _ in range(10)]

def makeNumber(idx, num, isMax=False):
  if len(num) == k+1:
    return num
  
  result = None

  if isMax:
    for i in range(9, -1, -1):
      if visited[i]: continue
      if A[idx] == '>':
        if i < int(num[-1]):
          visited[i] = True
          result = makeNumber(idx + 1, num + str(i), isMax)
          if result: return result
          visited[i] = False
      else:
        if i > int(num[-1]):
          visited[i] = True
          result = makeNumber(idx + 1, num + str(i), isMax)
          if result: return result
          visited[i] = False
  else:
    for i in range(10):
      if visited[i]: continue

      if A[idx] == '>':
        if i < int(num[-1]):
          visited[i] = True
          result = makeNumber(idx + 1, num + str(i))
          if result: return result
          visited[i] = False
      else:
        if i > int(num[-1]):
          visited[i] = True
          result = makeNumber(idx + 1, num + str(i))
          if result: return result
          visited[i] = False

for i in range(9, -1, -1):
  visited[i] = True
  num = makeNumber(0, str(i), True)
  if num:
    print(num)
    break
  visited[i] = False

visited = [False for _ in range(10)]

for i in range(10):
  visited[i] = True
  num = makeNumber(0, str(i))
  if num:
    print(num)
    break
  visited[i] = False

