N,M,K = map(int,input().split())

board = [[0 for _ in range(M)] for _ in range(N)]
stickers = []

for _ in range(K):
  r,c = map(int,input().split())
  sticker = []
  for _ in range(r):
    sticker.append(list(map(int,input().split())))

  stickers.append(sticker)

def isStickerFit(R,C,sticker):
  for r in range(len(sticker)):
    for c in range(len(sticker[0])):
      nr = r + R
      nc = c + C
      if 0 <= nr < N and 0 <= nc < M: 
        if sticker[r][c] == 1 and board[nr][nc] == 1: return False
        continue
      else:
        return False
  return True

def fillSticker(R,C,sticker):
  for r in range(len(sticker)):
    for c in range(len(sticker[0])):
      nr = r + R
      nc = c + C
      if sticker[r][c]:
        board[nr][nc] = 1

k = 0
while k < K:
  isSticked = False
  cur_sticker = stickers[k]
  for rotate in range(4):
    if isSticked: break
    r_sticker = cur_sticker
    for _ in range(rotate):
      r_sticker = list(zip(*r_sticker[::-1]))
    for r in range(N):
      for c in range(M):
        if isSticked: break
        if isStickerFit(r,c, r_sticker):
          fillSticker(r,c, r_sticker)
          k += 1
          isSticked = True
          break
  if not isSticked:
    k += 1

count = 0
for i in range(N):
  for j in range(M):
    count += board[i][j]

print(count)
