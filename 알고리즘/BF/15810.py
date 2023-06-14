N,M = map(int,input().split())
A = list(map(int,input().split()))

left = 0
right = 10**12 + 1
answer = None

while left <= right:
  mid = (left + right) // 2
  total = 0 # mid 시간까지 만들 수 있는 풍선의 개수

  for m in A:
    total += mid // m
  
  if total >= M: # mid 시간까지 M개 보다 더 많이 만들었다면, 시간을 줄여줘
    answer = mid
    right = mid - 1
  else: # mid 시간까지 M개 보다 덜 만들었다면, 시간을 늘려줘
    left = mid + 1

print(answer)