from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
  r,c = map(int,input().split())
  board[r-1][c-1] = 1

l = int(input())
changes = deque()

for _ in range(l):
  x,c = input().split()
  changes.append([int(x),c])

time = 0

dir = [(-1,0), (0,1), (1,0), (0,-1)]

d = 1

snake = deque()
snake.append([0,0])

def changeDirection(c):
  global d
  if c == 'D':
    d = (d + 1) % 4
    return
  d -= 1
  if d < 0:
    d = 3
  return 

def moveSnake():
  headR, headC = snake[0]
  headR += dir[d][0]
  headC += dir[d][1]
  snake.appendleft([headR, headC])
  snake.pop()

def isCrashed(r,c):
  if [r,c] in snake:
    return True
  if 0 <= r < n and 0 <= c < n:
    return False
  return True

while True:
  time += 1

  headR, headC = snake[0]
  headR += dir[d][0]
  headC += dir[d][1]

  if isCrashed(headR, headC):
    break
  
  if board[headR][headC]:
    board[headR][headC] = 0
    tailR, tailC = snake[-1]
    moveSnake()
    snake.append([tailR, tailC])
  else:
    moveSnake()
  
  if changes and time == changes[0][0]:
    _, c = changes.popleft()
    changeDirection(c)

print(time)
