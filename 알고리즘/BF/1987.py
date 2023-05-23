from collections import defaultdict

import sys
input = sys.stdin.readline

# 파이썬은 배열 > set > defaultdict 순으로 인덱스 탐색 속도가 다르다!

R,C = map(int,input().split())

board = list(list(input().rstrip()) for _ in range(R))

dir = [(1,0), (-1,0), (0,1), (0,-1)]

alpha = set()

answer = 0

def backtrack(r,c, count):
  global answer
  answer = max(answer, count)
  if answer == 26:
    return

  for dr,dc in dir:
    nr,nc = r + dr, c + dc
    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in alpha:
      alpha.add(board[nr][nc])
      backtrack(nr,nc, count+1)
      alpha.remove(board[nr][nc])

alpha.add(board[0][0])

backtrack(0,0,1)

print(answer)