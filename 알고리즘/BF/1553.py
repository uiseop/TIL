dominos = []
answer = 0

for i in range(7):
  for j in range(i, 7):
    dominos.append([i,j])

def getRotates(domino):
  rotates = set()
  i,j = domino
  rotates.add((i,j))
  rotates.add((j,i))
  return rotates

def backtrack(r,c,count):
  global answer

  if r == 7 and c == 6:
    if count == 28:
      answer += 1
    return
  
  if checked[r][c]:
    return backtrack(r, c+1, count) if (c+1) % 7 != 0 else backtrack(r+1,0,count)
  
  for i in range(28):
    if visited[i]: continue
    rotates = getRotates(dominos[i])
    if c + 1 != 7 and not checked[r][c+1]:
      for left,right in rotates:
        if board[r][c] == left and board[r][c+1] == right:
          visited[i] = True
          checked[r][c] = True
          checked[r][c+1] = True
          backtrack(r, c+1, count+1) if (c+1) % 7 != 0 else backtrack(r+1,0,count+1)
          visited[i] = False
          checked[r][c] = False
          checked[r][c+1] = False
    
    if r + 1 != 8 and not checked[r+1][c]:
      for top,bottom in rotates:
        if board[r][c] == top and board[r+1][c] == bottom:
          visited[i] = True
          checked[r][c] = True
          checked[r+1][c] = True
          backtrack(r, c+1, count+1) if (c+1) % 7 != 0 else backtrack(r+1,0,count+1)
          visited[i] = False
          checked[r][c] = False
          checked[r+1][c] = False

board = []
visited = [False for _ in range(28)]
checked = [[False for _ in range(7)] for _ in range(8)]

for _ in range(8):
  board.append(list(map(int, list(input()))))

backtrack(0,0,0)

print(answer)