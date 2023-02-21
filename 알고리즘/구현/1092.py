import heapq
import sys

input = sys.stdin.readline

n = int(input())

crane = list(map(int, input().split()))
crane.sort()

m = int(input())

boxes = list(map(int,input().split()))
boxes.sort(key=lambda x:-x)

cnt = 0
time = 0
b_visited = [False for _ in range(m)]
c_pos = [0 for _ in range(n)]

if max(boxes) > max(crane):
    print(-1)
    exit()

while cnt < m:
    time += 1

    for i in range(n):
        for bid in range(c_pos[i], m):
            if boxes[bid] <= crane[i] and not b_visited[bid]:
                b_visited[bid] = True
                c_pos[i] = bid+1
                cnt += 1
                break
        else:
            c_pos[i] = m
print(time)