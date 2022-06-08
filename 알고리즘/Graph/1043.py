import sys

input = sys.stdin.readline

n,m = map(int,input().split())

truth = list(map(int,input().split()))[1:]
know = [False for _ in range(n+1)]
for t in truth:
    know[t] = True

lst = []

for _ in range(m):
    inComes = list(map(int,input().split()))[1:]
    
    for i in inComes:
        if know[i]:
            for j in inComes:
                know[j] = True
            break
    else:
        lst.append(inComes)

answer = 0

for inComes in lst:
    for i in inComes:
        if know[i]:
            for j in inComes:
                know[j] = True
            break
    else:
        answer += 1

print(know)

print(answer)

