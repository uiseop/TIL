N = int(input())

nums = ['1','2','3']

init = ''

def backtrack(words, l):
  if l == N:
    print(int(words))
    return True
  
  for num in nums:
    temp = words + num
    maxLength = len(temp) // 2
    for i in range(1, maxLength + 1):
      if temp[-2*i:-1*i] == temp[-1*i:]: break
    else:
      if backtrack(temp, l+1): return True
  return False

backtrack(init, 0)