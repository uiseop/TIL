from collections import defaultdict, deque
import sys

input = sys.stdin.readline

n, k = map(int,input().split())
while n != 0 and k != 0:
    nums = list(map(int,input().split()))

    dq = deque()
    temp = [nums[0]]
    dic = {}
    for num in nums:
        dic[num] = {
            'root': None,
            'childrenCnt': 0,
            'children': [],
            'value': num
        }

    for idx in range(1, len(nums)):
        if nums[idx] == nums[idx-1] + 1:
            temp.append(nums[idx])
        else:
            if temp:
                dq.append(temp)
            temp = [nums[idx]]
    if temp:
        dq.append(temp)
    
    root = dq.popleft()[0]
    rq = deque()

    while dq:
        nodes = dq.popleft()
        dic[root]["childrenCnt"] = len(nodes)
        dic[root]["children"] = nodes
        for node in nodes:
            dic[node]["root"] = root
            rq.append(node)
        root = rq.popleft()
    
    parentK = dic[k]["root"]
    answer = 0
    if not parentK:
        print(answer)
    else:
        grandParentK = dic[parentK]["root"]
        if not grandParentK:
            print(answer)
        else:
            uncles = dic[grandParentK]["children"]
            for uncle in uncles:
                if dic[uncle]["value"] == dic[parentK]["value"]:
                    continue
                answer += dic[uncle]["childrenCnt"]

            print(answer)

    n, k = map(int,input().split())