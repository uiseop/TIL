def check(arr, idx):

    for k in range(idx//2 + 1):
        if arr[idx-k: idx+1] == arr[idx-(2*k + 1):idx-k]:
            return False
    return True


def DFS(count):
    if not check(ans, count-1):
        return -1
 
    if count == n:
        print(*ans, sep="")
        return 0

    for num in nums:
        ans.append(num)
        if DFS(count + 1) == 0:
            return 0
        ans.pop()

n = int(input())

nums = [1,2,3]
ans = [1]

DFS(1)

# 백트랙킹의 과정에 대해 다시한번 공부할 수 있었음. 규칙대로 진행하다가 막히면 다시 돌아가는 
# for num in nums:
#     ans.append(num)
#     if DFS(count + 1) == 0:
#         return 0
#     ans.pop()
# 이 과정을 빼먹었던것이 큼 큼큼..
# ✅ 파이썬에서는 -1또한 True로 여긴다. 미친것같다.