import heapq

N = int(input())

lectures = []

for _ in range(N):
  inputs = list(map(int,input().split()))
  lectures.append(inputs)

lectures.sort(key=lambda x: x[1])

heap = []
answer = 0

for id, start, end in lectures:
  while heap and heap[0][0] <= start:
    heapq.heappop(heap)
  heapq.heappush(heap, [end, start])
  
  answer = max(answer, len(heap))

print(answer)