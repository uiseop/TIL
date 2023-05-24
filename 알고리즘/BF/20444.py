n,k = map(int,input().split())

left = 0
right = n
flag = False

def calc(c):
  return (c+1) * (n-c+1)

while left <= right:
  mid = ((left + right) // 2)

  counts = calc(mid)
  if counts == k:
    flag = True
    break

  if counts < k:
    left = mid + 1
  else:
    right = mid - 1

print("YES") if flag else print("NO")