from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

maze = list(list(map(int,list(input().rstrip()))) for _ in range(n))
dir = [(1,0), (-1,0), (0,1), (0,-1)]

def BFS(row,col):
    dq = deque()
    dq.append([row,col])

    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1

    while dq:
        r,c = dq.popleft()

        if r == n-1 and c == m-1:
            print(visited[r][c])
            return

        for dr,dc in dir:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and maze[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                dq.append([nr,nc])

BFS(0,0)