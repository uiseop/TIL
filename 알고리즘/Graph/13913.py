from collections import deque
import sys

input = sys.stdin.readline

n,k = map(int,input().split())

q = deque()
q.append([n, 0])
visited = [-1 for _ in range(100001)]

def move(pos, n):
    answer = []
    temp = pos
    while temp != n:
        answer.append(temp)
        temp = visited[temp]
    answer.append(n)
    return " ".join(map(str,answer[::-1]))

while q:
    pos, cnt = q.popleft()
    if pos == k:
        print(cnt)
        print(move(pos, n))
        break

    for n_pos in (pos-1, pos+1, pos*2):
        if 0 <= n_pos <= 100000 and visited[n_pos] == -1:
            q.append([n_pos, cnt + 1])
            visited[n_pos] = pos
