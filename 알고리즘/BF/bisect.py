from bisect import bisect_left
from collections import defaultdict


a = [100,100,50,40,40,20,10]
player = [5,25,50,120]

def solve(ranked, player):
  ranks = defaultdict(int)

  curRank = 1
  for rank in ranked:
    if not ranks[rank]:
      ranks[rank] = curRank
      curRank += 1
  
  print(ranks)

  ranked.reverse()
  print(ranked)
  result = []

  for point in player:
    idx = bisect_left(ranked, point)
    if idx == len(ranked):
      result.append(1)
    else:
      if point == ranked[idx]:
        result.append(ranks[point])
      else:
        result.append(ranks[ranked[idx]] + 1)
  
  print(result)


solve(a, player)