n = int(input())

impossible_cache = set()

def getSangGeunSoo(num, cache):
  s_num = str(num)

  if num == 1:
    return True

  if num in cache or num in impossible_cache:
    for n in cache:
      impossible_cache.add(n)
    return False
  
  n_num = 0
  for n in s_num:
    n_num += int(n) ** 2
  cache.add(num)

  return getSangGeunSoo(n_num, cache)

def getPrimes(n):
  a = [False,False] + [True]*(n-1)
  primes=[]

  for i in range(2,n+1):
    if a[i]:
      primes.append(i)
      for j in range(2*i, n+1, i):
          a[j] = False

  return primes

primes = getPrimes(n)
answer = []

for num in primes:
  if getSangGeunSoo(num, set()):
    answer.append(num)

for num in answer:
  print(num)

