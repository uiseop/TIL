from math import ceil
import sys

input = sys.stdin.readline

n = int(input())

partis = list(map(int,input().split()))

b,c = map(int,input().split())

num = 0

for parti in partis:
    rest = parti - b
    num += 1
    if rest > 0:
        num += ceil(rest / c)

print(num)