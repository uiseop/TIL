import sys

input = sys.stdin.readline

N,M = map(int,input().split())

parents = [i for i in range(N+1)]

T = list(map(int,input().split()))[1:]

def union(a,b):
    a = find(a)
    b = find(b)
    if a in T and b in T:
        return
    
    if a in T:
        parents[b] = a
        T.append(b)
    elif b in T:
        parents[a] = b
        T.append(a)
    else:
        if a < b:
            parents[b] = a
        else:
            parents[a] = b

def find(a):
    if a == parents[a]:
        return a
    parents[a] = find(parents[a])
    return parents[a]

parties = []

for _ in range(M):
    participants = list(map(int,input().split()))
    parties.append(participants[1:])
    for p in range(1, participants[0]):
        union(participants[p], participants[p+1])

answer = 0

for party in parties:
    for p in party:
        if find(p) in T:
            break
    else:
        answer += 1

print(answer)