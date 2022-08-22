import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

def backTracking(i, cakes, before):
    if i == n:
        for cake in cakes:
            print(cake)
        exit()
    for cake in day[i]:
        if cake != before and not ate[i][cake-1]:
            ate[i][cake-1] = True
            backTracking(i+1, cakes + [cake], cake)


n = int(input())

day = []

for _ in range(n):
    a = list(map(int,input().split()))[1:]
    day.append(a)

ate = {i: [False for _ in range(10)] for i in range(n)}
backTracking(0, [], 0)

print(-1)