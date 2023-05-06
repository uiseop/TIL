import sys

input = sys.stdin.readline

n,m = map(int,input().split())

board = list(list(map(int,input().split())) for _ in range(n))

dir = [(1,0), (-1,0), (0,1), (0,-1)]

visited = [[-1 for _ in range(m)] for _ in range(n)]

answer = 0

def dfs(curHeight, r,c):
  global answer
  if r == n-1 and c == m-1:
    return 1
  
  if visited[r][c] != -1:
    return visited[r][c]
  
  visited[r][c] = 0
  for dr,dc in dir:
    nr,nc = r + dr, c + dc
    if 0 <= nr < n and 0 <= nc < m and board[nr][nc] < curHeight:
      visited[r][c] += dfs(board[nr][nc], nr,nc)
  
  return visited[r][c]

dfs(board[0][0], 0,0)

print(visited[0][0])