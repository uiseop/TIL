N = int(input())

nums = list(map(int,input().split()))

left = 0
right = len(nums) - 1

answer = [float("INF"), 0,0]

while left < right:
  cur = nums[left] + nums[right]
  if cur == 0:
    answer = [0, nums[left], nums[right]]
    break

  if abs(cur) < abs(answer[0]):
    answer = [cur, nums[left], nums[right]]

  if cur > 0:
    right -= 1
  else:
    left += 1

print(answer[1], answer[2])