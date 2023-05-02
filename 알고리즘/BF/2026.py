from collections import defaultdict


k,n,f = map(int,input().split())

edges = defaultdict(list)

for _ in range(f):
  v1,v2 = map(int,input().split())
  edges[v1-1].append(v2-1)
  edges[v2-1].append(v1-1)

for i in range(n):
  edges[i].sort()

def isNodeHasNoLessThanK(node):
  if len(edges[node]) < k-1:
    return False
  return True

def isAllFriends(node, friends):
  for friend in friends:
    if friend in edges[node]:
      continue
    return False
  return True

def findFriends(node, friends):
  # Greedy 방식
  # friends = set([node])
  # for friend in edges[node]:
  #   if friend in friends: continue
  #   if len(friends) == k:
  #     return friends
  #   if isNodeHasNoLessThanK(friend) and isAllFriends(friend, friends):
  #     friends.add(friend)
  # return friends

  if len(friends) == k:
    return True

  for nextNode in edges[node]:
    if nextNode in friends or visited[nextNode]: continue
    if isNodeHasNoLessThanK(nextNode) and isAllFriends(nextNode, friends):
      friends.add(nextNode)
      if findFriends(nextNode, friends):
        return True
      friends.remove(nextNode)

  return False

def printFriends(friends):
  for friend in friends:
    print(friend+1)

# visited = [False for _ in range(n)]

for i in range(n):
  if isNodeHasNoLessThanK(i):
    # visited[i] = True
    friends = set([i])
    findFriends(i, friends)
    if len(friends) == k:
      printFriends(friends)
      break
else:
  print(-1)