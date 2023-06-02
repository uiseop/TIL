from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

board = list(list(input().rstrip()) for _ in range(n))

visited = set()

def getPosition(r1,c1, r2,c2):
  return str(r1) + str(c1) + str(r2) + str(c2)

dir = [(1,0), (-1,0), (0,1), (0,-1)] # 0: bottom, 1: top, 2: right, 3: left 
inf = float("INF")


def moveRow(r,c,d):
  while True:
    nr = r + dir[d][0]
    nc = c + dir[d][1]
    if board[nr][nc] == '.':
      r = nr
      continue
    if board[nr][nc] == 'O':
      return False
    if board[nr][nc] == '#':
      break
  return r

def moveCol(r,c,d):
  while True:
    nr = r + dir[d][0]
    nc = c + dir[d][1]
    if board[nr][nc] == '.':
      c = nc
      continue
    if board[nr][nc] == 'O':
      return False
    if board[nr][nc] == '#':
      break
  return c



def tiltTop(r1,c1,r2,c2,cnt):
  if c1 == c2: # 같은 열이라면
    if r1 < r2: # 빨강이 더 위에 있다면
      r1 = moveRow(r1,c1, 1)
      r2 = moveRow(r2,c2, 1)
      if not r1: return
      q.append([r1,c1, r2,c2, cnt+1])
    else: # 빨강이 더 아래에 있다면
      r2 = moveRow(r2,c2, 1)
      r1 = moveRow(r1,c1, 1)
      if not r2: return
      q.append([r1,c1, r2,c2, cnt+1])
  else:
    r1 = moveRow(r1,c1, 1)
    r2 = moveRow(r2,c2, 1)
    if not r2: return
    if not r1:
      q.append([er,ec,r2,c2,cnt+1])
      return
    q.append([r1,c1,r2,c2,cnt+1])
    

def tiltDown(r1,c1,r2,c2,cnt):
  if c1 == c2: # 같은 열이라면
    if r1 > r2: # 빨강이 더 위에 있다면
      r2 = moveRow(r2,c2,0)
      r1 = moveRow(r1,c1,0)
      if not r2: return
      q.append([r1,c1, r2,c2, cnt+1])
    else: # 빨강이 더 아래에 있다면
      r1 = moveRow(r1,c1,0)
      r2 = moveRow(r2,c2,0)
      if not r2: return
      q.append([r1,c1, r2,c2, cnt+1])
  else:
    r1 = moveRow(r1,c1,0)
    r2 = moveRow(r2,c2,0)
    if not r2: return
    if not r1:
      q.append([er,ec,r2,c2,cnt+1])
      return
    q.append([r1,c1,r2,c2,cnt+1])

def tiltRight(r1,c1,r2,c2,cnt):
  if r1 == r2: # 같은 행이라면
    if c1 > c2: # 빨강이 더 오른쪽에 있다면
      c1 = moveCol(r1,c1,2)
      c2 = moveCol(r2,c2,2)
      if not c1: return
      q.append([r1,c1,r2,c2,cnt+1])
    else: # 빨강이 더 왼쪽에 있다면
      c2 = moveCol(r2,c2,2)
      c1 = moveCol(r1,c1,2)
      if not c2: return
      q.append([r1,c1,r2,c2,cnt+1])
  else:
    c1 = moveCol(r1,c1,2)
    c2 = moveCol(r2,c2,2)
    if not c2: return
    if not c1:
      q.append([er,ec,r2,c2,cnt+1])
      return
    q.append([r1,c1,r2,c2,cnt+1])

def tiltLeft(r1,c1,r2,c2,cnt):
  if r1 == r2: # 같은 행이라면
    if c1 > c2: # 빨강이 더 오른쪽에 있다면
      c2 = moveCol(r1,c1,3)
      c1 = moveCol(r2,c2,3)
      if not c2: return
      q.append([r1,c1,r2,c2,cnt+1])
    else: # 빨강이 더 왼쪽에 있다면
      c1 = moveCol(r1,c1,3)
      c2 = moveCol(r2,c2,3)
      if not c2: return
      q.append([r1,c1,r2,c2,cnt+1])
  else:
    c1 = moveCol(r1,c1,3)
    c2 = moveCol(r2,c2,3)
    if not c2: return
    if not c1:
      q.append([er,ec,r2,c2,cnt+1])
      return
    q.append([r1,c1,r2,c2,cnt+1])
  

q = deque()

r1,c1,r2,c2,er,ec = None,None,None,None,None,None # Red: r1,c1 Blue: r2,c2

for i in range(1, n-1):
  for j in range(1, m-1):
    if board[i][j] == 'R':
      r1,c1 = i,j  
      board[i][j] = '.'
    elif board[i][j] == 'B':
      r2,c2 = i,j
      board[i][j] = '.'
    elif board[i][j] == 'O':
      er,ec = i,j

q.append([r1,c1,r2,c2,0])

while q:
  r1,c1,r2,c2,cnt = q.popleft()
  if cnt > 10:
    break
  if r1 == er and c1 == ec:
    print(cnt)
    break
  tiltTop(r1,c1,r2,c2,cnt)
  tiltDown(r1,c1,r2,c2,cnt)
  tiltRight(r1,c1,r2,c2,cnt)
  tiltLeft(r1,c1,r2,c2,cnt)
