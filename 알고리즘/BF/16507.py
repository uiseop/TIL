from itertools import accumulate
import sys

input = sys.stdin.readline

r,c,q = map(int,input().split())

p_sum = [[0 for _ in range(c+1)]]

for _ in range(r):
    num_list = [0] + list(map(int,input().split()))
    p_sum.append(list(accumulate(num_list)))


for row in range(1,r+1):
    for col in range(1,c+1):
        p_sum[row][col] += p_sum[row-1][col]

for i in range(q):
    r1,c1, r2,c2 = map(int,input().split())
    ans = p_sum[r2][c2] - p_sum[r1-1][c2] - p_sum[r2][c1-1] + p_sum[r1-1][c1-1]
    print(ans // ((r2-r1+1) * (c2-c1+1)))