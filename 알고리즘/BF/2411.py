from collections import deque


N,M,A,B = map(int,input().split())

board = [[0 for _ in range(M)] for _ in range(N)]

items = []

for _ in range(A):
  r,c = map(int,input().split())
  r -= 1
  c -= 1

  board[r][c] = 1
  items.append([r,c])

for _ in range(B):
  r,c = map(int,input().split())
  r -= 1
  c -= 1

  board[r][c] = 2

items.sort(key=lambda x: [x[1], x[0]])

dir = [(1,0), (0,1)]

def countRoutes(r1,c1, r2,c2, board):
  count = 0
  if r1 == r2 and c1 == c2:
    return 1

  for dr,dc in dir:
    nr = r1 + dr
    nc = c1 + dc
    if nr <= r2 and nc <= c2 and board[nr][nc] != 2:
      count += countRoutes(nr,nc, r2,c2, board)
  
  return count

r,c = 0,0

answer = 1

for nr,nc in items:
  answer *= countRoutes(r,c, nr,nc, board)
  r,c = nr,nc

answer *= countRoutes(r,c, N-1, M-1, board)

print(answer)