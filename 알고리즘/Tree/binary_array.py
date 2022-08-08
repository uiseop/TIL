import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

left = [0] * (n+1)
right = [0] * (n+1)

visitCount = 0

for _ in range(n):
    root, left, right = map(int, input().split())
    left[root] = left
    right[root] = right

ans = 0

def traverse(cur):
    global ans, visitCount
    if left[cur] != -1:
        ans += 1
        traverse(left[cur])
        ans += 1
    visitCount += 1
    if right[cur] != -1:
        ans += 1
        traverse(right[cur])
        if visitCount == n: return
        ans += 1
        
traverse(1)
print(ans)