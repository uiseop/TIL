import heapq
import sys

input = sys.stdin.readline

T = int(input())
Case = 1

dr = [1,-1,0,0]
dc = [0,0,1,-1]

while T:
    gool = []
    for _ in range(T):
        gool.append(list(map(int, input().split())))
    
    visited = [[False] * T for _ in range(T)]
    heap = [[gool[0][0], 0,0]]
    visited[0][0] = True
    while heap:
        k,r,c = heapq.heappop(heap)
        if r == T-1 and c == T-1:
            print(f"Problem {Case}: {k}")
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < T and 0 <= nc < T and not visited[nr][nc]:
                heapq.heappush(heap, [k + gool[nr][nc], nr, nc])
                visited[nr][nc] = True

    Case += 1
    T = int(input())