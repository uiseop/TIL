import heapq
import sys

input = sys.stdin.readline

N,M,K = map(int,input().split())

maze = [list(map(int,list(input().rstrip()))) for _ in range(N)]

heap = []

heapq.heappush(heap, [0,0,0,0]) # step, k, r,c

visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(K+1)]

for k in range(K):
    visited[k][0][0] = True

dr = [1,-1,0,0]
dc = [0,0,1,-1]

while heap:
    step, k, r, c = heapq.heappop(heap)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not visited[k][nr][nc]:
            if nr == N-1 and nc == M-1:
                print(step + 1, k)
                exit()
            if maze[nr][nc] == 1 and k < K:
                heapq.heappush(heap, [step+1, k+1, nr,nc])
                visited[k+1][nr][nc] = True
            else:
                heapq.heappush(heap, [step+1, k, nr,nc])
                visited[k][nr][nc] = True
