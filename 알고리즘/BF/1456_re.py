A,B = map(int,input().split())

def bisec(nums, target):
  left = 0
  right = len(nums) - 1
  while left <= right:
    mid = (left + right) // 2
    if nums[mid] < target:
      left = mid + 1
    elif nums[mid] > target:
      right = mid - 1
    else:
      return mid
  
  if right < 0:
    return 0
  if left >= len(nums):
    return len(nums) - 1
  
  return left if target - nums[right] > nums[left] - target else right

MAX_NUMBER = 10**7 + 1
visited = [True] * MAX_NUMBER

primes = []

for i in range(2, MAX_NUMBER):
  if not visited[i]:
    continue
  if i**2 > B:
    break

  primes.append(i)
  for j in range(i**2, MAX_NUMBER, i): # 찾은 소수의 n배수를 모두 False 처리해서 불필요한 방문 X
    visited[j] = False
