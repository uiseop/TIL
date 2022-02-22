import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(frm):
    if not tree[frm]:
        return
    for to,weight in tree[frm]:
        dfs(to)
        if sumList[to]:
            weight += -sumList[to][0]
        heapq.heappush(sumList[frm], -weight)
    return

n = int(input())
if n == 1:
    print(0)
    exit()
tree = [[] for _ in range(n + 1)]
sumList = [[] for _ in range(n + 1)]
for _ in range(n-1):
    frm, to, weight = map(int,input().split())
    tree[frm].append([to, weight])

dfs(1)
ans = -sumList[1][0]
# ⬆️ 반례 해결. 일자 트리일 때를 확인을 안함... ㄷㄷ
# 5
# 1 2 10
# 2 3 10
# 3 4 10
# 4 5 10
for sums in sumList:
    if len(sums) >= 2:
        first = -heapq.heappop(sums)
        second = -heapq.heappop(sums)
        if ans < first + second:
            ans = first + second

print(ans)
# dfs(1)

# for t in tree:
#     print(t)
# []
# [[2, 3], [3, 2]]
# [[4, 5]]
# [[5, 11], [6, 9]]
# [[7, 1], [8, 7]]
# [[9, 15], [10, 4]]
# [[11, 6], [12, 10]]
# []
# []
# []
# []
# []
# []

