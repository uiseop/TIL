C = int(input())

def dfs(pos, count, total):
  answer = 0
  if pos == 11:
    if count == 11:
      return total
    return answer
  
  for player in possibles[pos]:
    if selected[player]: continue
    selected[player] = True
    answer = max(answer, dfs(pos+1, count+1, total + players[player][pos]))
    selected[player] = False
  
  return answer

for _ in range(C):
  players = list(list(map(int,input().split())) for _ in range(11))

  possibles = [[] for _ in range(11)]

  for i in range(11):
    for j in range(11):
      if players[i][j]:
        possibles[j].append(i)
  
  selected = [False for _ in range(11)]

  print(dfs(0, 0, 0))
