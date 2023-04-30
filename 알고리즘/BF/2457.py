import sys
input = sys.stdin.readline

n = int(input())

flowers = []

for _ in range(n):
  sm, sd, em, ed = map(int,input().split())
  sDay = sm * 100 + sd
  eDay = em * 100 + ed
  flowers.append([sDay, eDay])

flowers.sort(key=lambda x: x[0])

startIndex = 0
temp = []
now = 301
answer = 0

while True:

  for i in range(startIndex, n):
    if flowers[i][0] <= now and flowers[i][1] > now:
      temp.append(flowers[i][1])
      startIndex += 1
    
  if temp:
    now = max(temp)
    answer += 1
    temp = []
  else:
    break
  if now >= 1201:
    break

if now >= 1201:
  print(answer)
else:
  print(0)