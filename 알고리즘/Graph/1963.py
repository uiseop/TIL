from collections import deque
import sys


def isPrime(num):
    for i in range(2,num+1):
        if i**2 >= num: break
        if num % i == 0: return False
    return True

def findCnt3(num, idx,c_primes):
    result = []
    l_num = list(str(num))
    for prime in c_primes:
        l_prime = list(str(prime))
        cnt = 0
        for i in range(4):
            if l_num[i] == l_prime[i]:
                cnt += 1
        if cnt == 3:
            result.append([prime, idx])
    for prime,i in result:
        c_primes.remove(prime)
    return result

primes = []

for i in range(1000, 10000):
    if isPrime(i):
        primes.append(i)

input = sys.stdin.readline
T = int(input())
flag = False

for _ in range(T):
    n,m = map(int,input().split())
    c_primes = primes.copy()
    q = deque()
    q.append([n,0])
    q += findCnt3(n,1,c_primes)
    while q:
        prime, idx = q.popleft()
        if prime == m:
            flag = True
            print(idx)
            break
        q += findCnt3(prime, idx + 1,c_primes)

if not flag:
    print("Impossible")

