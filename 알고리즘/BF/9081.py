

T = int(input())

def dfs(i, visited, strings, cur, origin):
  if len(cur) == len(strings) and cur != ''.join(origin):
    print(cur)
    return True
  if cur < ''.join(origin[:len(cur)]):
    return False
  
  for nid in range(len(strings)):
    if visited[nid]: continue
    visited[nid] = True
    if dfs(nid, visited, strings, cur + strings[nid], origin):
      return True
    visited[nid] = False


for _ in range(T):
  strings = list(input())
  s_strings = sorted(strings)
  visited = [False for _ in range(len(strings))]

  for i in range(len(s_strings)):
    visited[i] = True
    if dfs(i, visited, s_strings, s_strings[i], strings):
      break
    visited[i] = False
  else:
    print(''.join(strings))