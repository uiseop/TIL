from collections import defaultdict, deque
import sys

input = sys.stdin.readline

while True:
    n,k = map(int,input().split())
    if n == 0 and k == 0:
        break
    nums = list(map(int,input().split()))
    if n == 1:
        print(0)
    level = defaultdict(list)
    level[nums[0]], level[nums[1]] = [0,1], [1,1]
    level_cnt = [1]
    graph = deque([nums[0]])
    cur = 0
    brothers = []
    childes = defaultdict(list)
    parents = defaultdict(list)
    parent = nums[0]
    for i in range(1,n):
        if nums[i] == nums[i-1] + 1:
            brothers.append(nums[i])
        else:
            for b in brothers:
                level[b].append(len(brothers))
            brothers = [nums[i]]
            parent = graph.popleft()
            cur = level[parent][0] + 1
        if len(level_cnt) - 1 < cur:
            level_cnt.append(1)
        else:
            level_cnt[-1] += 1 
        level[nums[i]] = [cur]
        graph.append(nums[i])
        childes[parent] .append(nums[i])
        parents[nums[i]] = parent
        
    for b in brothers:
        level[b].append(len(brothers))
    
    p = parents[k]
    pp = parents[p]
    cnt = 0
    cc = childes[pp]
    for c in cc:

    print(level_cnt[level[k][0]] - level[k][1])


