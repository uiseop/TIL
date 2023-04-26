from collections import defaultdict
import sys

input = sys.stdin.readline

n,d,k,c = map(int,input().split())

sushi = []

for _ in range(n):
    sushi.append(int(input()))

sushi.extend(sushi)

left = 0
max_cnt = 0
eat = defaultdict(int)

eat[c] += 1

for right in range(len(sushi)):
    ate = sushi[right]

    eat[ate] += 1

    if right >= k-1:
        max_cnt = max(max_cnt, len(eat))
        pop_ate = sushi[left]
        eat[pop_ate] -= 1
        if eat[pop_ate] == 0:
            del eat[pop_ate]
        left += 1

print(max_cnt)