import sys

input = sys.stdin.readline

n,m = map(int,input().split())

parent = [i for i in range(n+1)]
truth = list(map(int,input().split()))[1:]
answer = 0

for t in truth:
    parent[t] = t

def find(a):
    if a == parent[a]:
        return parent[a]
    parent[a] = find(parent[a])
    return parent[a] 

def union(a,b):
    a = find(a)
    b = find(b)

    if a in truth and b in truth:
        return 

    if a in truth:
        parent[b] = a
        truth.append(b)
    elif b in truth:
        parent[a] = b
        truth.append(a)
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

parties = []

for _ in range(m):
    participants = list(map(int,input().split()))
    for p in range(1,participants[0]):
        union(participants[p], participants[p+1])
    parties.append(participants[1:])

for party in parties:
    # print(party)
    for i in party:
        if parent[i] in truth:
            break
    else:
        answer += 1

# print(truth)

print(answer)