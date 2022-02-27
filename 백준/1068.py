import sys

def dfs(node):
    global ans
    if node == target:
        if node != root:
            ans += 1
        return
    if not tree[node]:
        ans += 1
        return
    for i in tree[node]:
        dfs(i)
    

input = sys.stdin.readline
n = int(input())

inList = list(map(int,input().split()))
tree = [[] for _ in range(n)]
target = int(input())
if inList[target] == -1:
    print(0)
    exit()
inList = inList[:target] + [-2] + inList[target+1:]
for i in range(len(inList)):
    if inList[i] < 0:
        if inList[i] == -1:
            root = i
        continue
    tree[inList[i]].append(i)


ans = 0
dfs(root)
print(ans)

