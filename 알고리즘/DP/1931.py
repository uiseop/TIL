import sys

input = sys.stdin.readline

N = int(input())

meetings = []

for _ in range(N):
    meetings.append(list(map(int,input().split())))

meetings.sort(key=lambda x: [x[1], x[0]])

finished = meetings[0][1]
result = 1

for start, finish in meetings[1:]:
    if finished <= start:
        finished = finish
        result += 1

print(result)