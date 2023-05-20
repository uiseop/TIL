import sys

input = sys.stdin.readline

R,C,k = map(int,input().split())

zido = list(list(input().rstrip()) for _ in range(R))

answer = 0

visited = [[False for _ in range(C)] for _ in range(R)]
visited[R-1][0] = True

dir = [[1,0], [-1,0], [0,1], [0,-1]]

def backtrack(r,c,cnt):
  global answer
  if r == 0 and c == C-1:
    if cnt == k:
      answer += 1
    return
  
  for dr,dc in dir:
    nr = r + dr
    nc = c + dc
    if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and zido[nr][nc] != 'T':
      visited[nr][nc] = True
      backtrack(nr,nc, cnt+1)
      visited[nr][nc] = False

backtrack(R-1,0,1)

print(answer)