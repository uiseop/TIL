import sys

input =  sys.stdin.readline

n,r,c = map(int,input().split())

result = 0

while n:
  n -= 1
  if 0 <= r < 2**n and 0 <= c < 2**n: # 1사분면
    continue
  elif 0 <= r < 2**n and 2**n <= c < 2**(n+1): # 2사분면
    result += 4**n
    c -= 2**n
  elif 2**n <= r < 2**(n+1) and 0 <= c < 2**n: # 3사분면
    result += 4**n * 2
    r -= 2**n
  else: # 4사분면
    result += 4**n * 3
    r -= 2**n
    c -= 2**n

print(result)