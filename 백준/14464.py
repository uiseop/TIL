import sys
import heapq

input = sys.stdin.readline

c,n = map(int,input().split())

teacher = [int(input()) for _ in range(c)]
teacher.sort()

student = [list(map(int,input().split())) for _ in range(n) ]
student.sort()

ans = 0
heap = []
j = 0
for i in teacher:
    while j < n and i >= student[j][0]:
        # 끝나는 시간을 기준으로 우선순위 정렬
        heapq.heappush(heap, student[j][::-1])
        j += 1
    # 끝나는 시간이 봐주는 시간보다 적으면 당연히 out
    while heap and heap[0][0] < i:
        heapq.heappop(heap)
    if heap:
        heapq.heappop(heap)
        ans += 1
    
print(ans)