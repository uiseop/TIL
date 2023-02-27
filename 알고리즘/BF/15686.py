from itertools import combinations
import sys

input = sys.stdin.readline

N,M = map(int,input().split())

city = [list(map(int,input().split())) for _ in range(N)]
chicken = []
house = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append([i,j])
        elif city[i][j] == 1:
            house.append([i,j])

combis = combinations(chicken, M)

answer = float('inf')

def distance(i,j,x,y):
    return abs(i-x) + abs(j-y)

def backtrack(combi):
    global answer
    result = 0
    for i,j in house:
        result += min(distance(i,j,x,y) for x,y in combi)
        if result > answer:
            return
    answer = min(answer, result)

for combi in combis:
    backtrack(combi)

print(answer)