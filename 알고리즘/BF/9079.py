from collections import deque
from copy import deepcopy

T = int(input())

def flip(value):
  if value == 'H': return 'T'
  return 'H'

def flipRow(coins, r):
  copyCoins = deepcopy(coins)
  for c in range(3):
    copyCoins[r][c] = flip(copyCoins[r][c])
  return copyCoins

def flipCol(coins, c):
  copyCoins = deepcopy(coins)
  for r in range(3):
    copyCoins[r][c] = flip(coins[r][c])
  return copyCoins

def flipLeftDae(coins,r=0,c=0): # \ 방향
  copyCoins = deepcopy(coins)
  for dr,dc in [(0,0), (1,1), (2,2)]:
    nr, nc = r + dr, c + dc
    copyCoins[nr][nc] = flip(copyCoins[nr][nc])
  return copyCoins

def flipRightDae(coins,r=0,c=2): # / 방향
  copyCoins = deepcopy(coins)
  for dr,dc in [(0,0), (1,-1), (2,-2)]:
    nr, nc = r + dr, c + dc
    copyCoins[nr][nc] = flip(copyCoins[nr][nc])
  return copyCoins
  
def isAllSame(coins):
  root = coins[0][0]

  for r in range(3):
    for c in range(3):
      if coins[r][c] == root: continue
      else: return False
  return True

def bfs(coin, coinSet):
  q = deque()
  q.append([coin, 0])

  while q:
    coin, cnt = q.popleft()
    if isAllSame(coin):
      return cnt
    
    for r in range(3):
      fliped = flipRow(coin, r)
      s_fliped = coin2String(fliped)
      if s_fliped not in coinSet:
        coinSet.add(s_fliped)
        q.append([fliped, cnt + 1])
    
    for c in range(3):
      fliped = flipCol(coin, c)
      s_fliped = coin2String(fliped)
      if s_fliped not in coinSet:
        coinSet.add(s_fliped)
        q.append([fliped, cnt + 1])
    
    fliped = flipLeftDae(coin)
    s_fliped = coin2String(fliped)
    if s_fliped not in coinSet:
      coinSet.add(s_fliped)
      q.append([fliped, cnt + 1])

    fliped = flipRightDae(coin)
    s_fliped = coin2String(fliped)
    if s_fliped not in coinSet:
      coinSet.add(s_fliped)
      q.append([fliped, cnt + 1])
  
  return -1

def coin2String(coin):
  coins = ''
  for r in range(3):
    for c in range(3):
      if coin[r][c] == 'H':
        coins += '1'
      else:
        coins += '0'
  return coins


for _ in range(T):
  coin = []
  coinSet = set()

  for r in range(3):
    lst = list(input().split())
    coin.append(lst)
  
  coinSet.add(coin2String(coin))
  
  print(bfs(coin, coinSet))

