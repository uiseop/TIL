import sys
import heapq

input = sys.stdin.readline

n = int(input())

# heap = []
left = float("inf")
cur = None
answer = []

for i in range(n):
    num = int(input())
    if not cur:
        cur = num
    else:
        if cur != num:
            if (left - cur > 0 and num - cur > 0):
                diff = min(left-cur, num-cur)
            elif left - cur > 0:
                diff = left-cur
            elif num - cur > 0: 
                diff = num - cur
            else:
                left = cur
                cur = num
                continue
            answer.append(diff)
            left = cur
            cur = num
        else:
            continue

# print(heap)
# # while len(heap) >= 2:
# #     num, diff = heapq.heappop(heap)
# #     answer += diff

# # print(answer)
print(sum(answer))