# 참고 : https://ahracho.github.io/posts/python/2017-05-09-python-integer-overflow/
#  from collections import defaultdict
# import math
# import sys

# input = sys.stdin.readline

# n = int(input())

# ns = list(map(int,input().split()))

# m = int(input())

# ms = list(map(int,input().split()))

# def multi(lst) :
#     result = 1
#     for i in range(len(lst)) :
#         result *= lst[i]
#     return result

# def gcd(a,b):
#     while b > 0 :
#         tmp = a%b
#         a = b
#         b = tmp
#     return a

# multi_n = multi(ns)
# multi_m = multi(ms)

# print(str(gcd(multi_n, multi_m))[-9:])



from collections import defaultdict
import sys

input = sys.stdin.readline

primes = []
visited = [False for _ in range(32000)]
for i in range(2, 32000):
    if visited[i]:
        continue
    primes.append(i)
    for j in range(2*i, 32000,i):
        visited[i] = True


def make(num, ch):
    if ch == 'a':
        for p in primes:
            if num % p == 0:
                a_dic[p] += 1
                make(num // p, 'a')
                return
        if num != 1:
            a_dic[num] += 1
    else:
        for p in primes:
            if num % p == 0:
                b_dic[p] += 1
                make(num // p, 'b')
                return
        if num != 1:
            b_dic[num] += 1


n = int(input())
ns = list(map(int,input().split()))
m = int(input())
ms = list(map(int,input().split()))

a_dic = defaultdict(int)
b_dic = defaultdict(int)

for n in ns:
    make(n, 'a')
for n in ms:
    make(n, 'b')


ans = 1
isBigger = False

for p in primes:
    if a_dic[p] and b_dic[p]:
        cnt = min(a_dic[p], b_dic[p])
        while cnt:
            cnt -= 1
            ans *= p
            if ans >= 1000000000:
                ans %= 1000000000
                isBigger = True

if isBigger:
    print(str(ans).zfill(9))
else:
    print(ans)