import sys

input = sys.stdin.readline

n = int(input())

arr = [0]

for _ in range(n):
    arr.append(int(input()))


answer = set()

def dfs(node, start ,routes):
    if node == start:
        for route in routes:
            answer.add(route)
        return

    if not visited[node]:
        visited[node] = True
        routes.append(node)
        dfs(arr[node], start, routes)


for i in range(1,n+1):
    if i in answer:
        continue
    visited = [False for _ in range(n+1)]
    visited[i] = True
    dfs(arr[i], i, [i])

answer = sorted(list(answer))
print(len(answer))
for node in answer:
    print(node)
