from collections import deque
import heapq
import sys

input = sys.stdin.readline

N,M,K = map(int,input().split())

rooms = list(list(input().rstrip()) for _ in range(N))

dq = deque([(1, 0, 0)]) # 이동 거리, n, m

visited = [[K + 1 for _ in range(M)] for _ in range(N)]
visited[0][0] = 0

dr = [1,-1,0,0]
dc = [0,0,1,-1]

# heap.push 시 O(log(N)) 만큼 시간 복잡도가 걸리기 떄문에 시간 초과가 발생하는 듯 함
# 반면 Queue의 경우 O(1) 밖에 걸리지 않기 때문에 시복잡 면에서 이득.
while dq:
    # p,n,m = heapq.heappop(heap)
    print(dq)
    p,n,m = dq.popleft()
    if n == N-1 and m == M-1:
        print(p)
        exit()
    for i in range(4):
        r = n + dr[i]
        c = m + dc[i]
        if 0 <= r < N and 0 <= c < M:
            tempK = visited[n][m] + int(rooms[r][c])
            if tempK < visited[r][c]:
                # heapq.heappush(heap, (p+1, r,c))
                dq.append((p+1, r,c))
                visited[r][c] = tempK    

print(-1)

