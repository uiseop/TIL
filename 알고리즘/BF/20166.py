N,M,K = map(int,input().split())

board = list(list(input()) for _ in range(N))

words = []
wordsCount = {}

for _ in range(K):
  word = input()
  words.append(word)
  wordsCount[word] = 0

dir = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]

def findRoots(word):
  roots = []
  for r in range(N):
    for c in range(M):
      if board[r][c] == word[0]:
        roots.append([r,c])
  return roots

def findWords(r,c,cur,target):
  if cur == target:
    wordsCount[target] += 1
    return
  
  curIndex = len(cur)

  for d in range(8):
    nr,nc = move(r,c,d)
    w = board[nr][nc]
    if w == target[curIndex]:
      findWords(nr,nc,cur + w, target)


def move(r,c,d):
  nr,nc = r + dir[d][0], c + dir[d][1]

  if nr >= N: nr = 0
  elif nr < 0: nr = N-1

  if nc >= M: nc = 0
  elif nc < 0: nc = M-1

  return [nr,nc]

for word in words:
  if wordsCount[word]: 
    print(wordsCount[word])
    continue

  roots = findRoots(word)

  for r,c in roots:
    cur = board[r][c]
    findWords(r,c,cur,word)
  print(wordsCount[word])
