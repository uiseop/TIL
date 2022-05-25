# 다익스트라 알고리즘은 최소 우선순위 큐를 사용해서 문제를 해결한다.
# 파이썬에서는 최소 우선순위 큐인 heapq를 기본 모듈로 제공한다.

import heapq

heap = []
heapq.heappush(heap, 100)
heapq.heappush(heap, 1)
heapq.heappush(heap, 10)
heapq.heappush(heap, 0)

print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)