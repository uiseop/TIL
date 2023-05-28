from collections import deque


dir = [(1,0), (-1,0), (0,1), (0,-1)]

size = input()
while size:
  row,col = map(int,size.split())
  board = list(list(input()) for _ in range(row))

  ball = [0,0]

  total = 0
  answer = 0
  visited = [[False for _ in range(col)] for _ in range(row)]

  flag = False
  for i in range(row):
    for j in range(col):
      if board[i][j] == '.' and not flag:
        ball = [i,j]
        flag = True
      elif board[i][j] == '.':
        total += 1
  
  ballRow, ballCol = ball[0], ball[1]
  visited[ballRow][ballCol] = True

  def backtrack(ball, d, moveCnt, cnt):
    global answer

    if cnt == total:
      answer = min(answer, moveCnt)
      return
    
    curCnt = 0
    q = deque()
    while True:
      nr = ball[0] + dir[d][0]
      nc = ball[1] + dir[d][1]
      if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc] and board[nr][nc] == '.':
        ball = [nr,nc]
        visited[nr][nc] = True
        q.append([nr,nc])
        curCnt += 1
      else:
        break

    if not curCnt: return

    for i in range(4):
      if i == d: continue
      backtrack(ball, i, moveCnt + curCnt, cnt + curCnt)
      while q:
        nr,nc = q.popleft()
        visited[nr][nc] = False

  for i in range(4):
    backtrack(ball, i, 0, 1)
    ball = [ballRow, ballCol]
  
  print(f'Case 1: {answer}')
  
  size = input()