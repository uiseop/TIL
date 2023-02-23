import sys

input = sys.stdin.readline

N,L = map(int,input().split())

heights = list(map(int,input().split()))

heights.sort()

for h in heights:
    if h <= L:
        L += 1
    else:
        break

print(L)