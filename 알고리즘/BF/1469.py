import sys

input = sys.stdin.readline

n = int(input())

x = list(map(int,input().split()))
x.sort()


def getRight(num, vid):
    return vid + num + 1

def backtrack(i):
    if i == n:
        print(*visited)
        exit()

    for vid in range(n*2):
        if visited[vid] == 'False':
            right = getRight(x[i], vid)
            if right >= n*2 or visited[right] != 'False':
                break
            visited[vid] = x[i]
            visited[right] = x[i]
            backtrack(i+1)
            visited[vid] = 'False'
            visited[right] = 'False'

visited = ['False' for _ in range(n*2)]

backtrack(0)

if 'False' in visited:
    print(-1)