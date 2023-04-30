import sys

input = sys.stdin.readline

n = int(input())

dotted = [[0 for _ in range(102)] for _ in range(100)]

for _ in range(n):
  x,y = map(int,input().split())
  for dx in range(10):
    for dy in range(1, 11):
      nx = x + dx
      ny = y + dy
      dotted[nx][ny] = 1

for i in range(1, 100): # row 0을 기준으로 높이 측정
  for j in range(1, 102):
    if dotted[i][j]:
      dotted[i][j] = dotted[i-1][j] + 1

answer = 0

for i in range(100):
  dotted_row = dotted[i]

  preColes = [0]

  for cur in range(1, 102):
    while preColes and dotted_row[preColes[-1]] > dotted_row[cur]: # 지금 높이가 더 낮다는 것은 새로운 사각형이 만들어 졌다는 뜻.
      # 이전의 모든 Col을 비교하면서 새로운 사각형을 찾음
      height = dotted_row[preColes[-1]]
      preColes.pop()
      answer = max(answer, (cur - preColes[-1] - 1) * height)
    preColes.append(cur)
  

print(answer)