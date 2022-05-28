import sys

input = sys.stdin.readline

n,m = map(int,input().split())
question = [0 for _ in range(n+1)]

for _ in range(m):
    pre,nxt = map(int,input().split())
    question[nxt] += 1
    