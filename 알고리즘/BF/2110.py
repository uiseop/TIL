N,C = map(int,input().split())

pos = list(int(input()) for _ in range(N))
pos.sort()

left = 0
right = 10**9 + 1
answer = 0

while left <= right: # right 
  count = 1
  mid = (left + right) // 2
  cur = pos[0]
  for x in pos[1:]:
    if x - cur >= mid:
      count += 1
      cur = x
  
  if count < C:
    right = mid - 1
  else:
    answer = mid
    left = mid + 1

print(answer)
