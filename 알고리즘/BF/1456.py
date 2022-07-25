import math
import sys

input = sys.stdin.readline

A,B = map(int,input().split())

max_num = 10**7 + 1
visted = [True] * max_num

primes = []

for i in range(2, max_num):
    if not visted[i]:
        continue
    if i**2 > B:
        break

    primes.append(i)
    for j in range(i**2, max_num, i): # 찾은 소수의 n배수를 모두 False 처리해서 불필요한 방문 X
        visted[j] = False

answer = 0

for prime in primes:
    temp = prime**2
    while temp <= B:
        if A <= temp:
            answer += 1
        temp *= prime

print(answer)
