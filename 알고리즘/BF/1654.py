K, N = map(int,input().split())

lans = list(int(input()) for _ in range(K))

left = 0
right = 2**31
answer = 0

while left <= right:
  mid = (left + right) // 2

  count = 0

  for lan in lans:
    count += lan  // mid
  
  if count < N:
    right = mid - 1
  else:
    left = mid + 1
    answer = mid

print(answer)

