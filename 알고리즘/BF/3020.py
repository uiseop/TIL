import heapq
import sys

input = sys.stdin.readline

N,H = map(int,input().split())

h = [0 for _ in range(H+1)]

for _ in range(N // 2):
    n = int(input())
    for i in range(1,n+1):
        h[i] += 1
    n = int(input())
    k = H - n + 1
    for i in range(k, H+1):
        h[i] += 1

heapq.heapify(h)
heapq.heappop(h)
min_val = h[0]
count = 0

while heapq.heappop(h) == min_val:
    count += 1

print(min_val, count)























import heapq
import sys

input = sys.stdin.readline

N,H = map(int,input().split())

bottom = [0 for _ in range(H+1)]
top = [0 for _ in range(H+1)]

for _ in range(N // 2):
    n = int(input())
    bottom[n] += 1
    n = int(input())
    top[n] += 1

for i in range(H-1, 0, -1):
    bottom[i] += bottom[i+1]
    top[i] += top[i+1]

minCount = N
count = 1

for i in range(1,H+1):
    if minCount > (bottom[i] + top[H-i+1]):
        minCount = (bottom[i] + top[H-i+1])
        count = 1
    elif minCount == (bottom[i] + top[H-i+1]):
        count += 1

print(minCount, count)
