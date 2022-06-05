import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

frinends = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    frinends[a].append(b)
    frinends[b].append(a)

invites = set()
invites.add(1)

for frined in frinends[1]:
    invites.add(frined)
    for n_friend in frinends[frined]:
        invites.add(n_friend)

print(len(invites) - 1)