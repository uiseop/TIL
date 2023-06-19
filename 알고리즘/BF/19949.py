from collections import deque


answer = list(map(int,input().split()))

def checkAnswer(idx, cur, q):
  result = 0
  
  if 10 - idx + cur < 5:
    return 0
  
  if idx == 10 and cur >= 5:
    return 1

  for i in range(1, 6):
    if q[-1] == q[-2] == i:
      continue
    q.append(i)
    if answer[idx] == i:
      result += checkAnswer(idx+1, cur + 1, q)
    else:
      result += checkAnswer(idx+1, cur, q)
    q.pop()

  
  return result

print(checkAnswer(0, 0, deque([0, 0])))