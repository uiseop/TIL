import heapq

n,m = map(int,input().split())
jido = []
for _ in range(n):
    jido.append(list(map(int,input().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

heap = []
heapq.heappush(heap, (-jido[0][0], 0, 0))
visited[0][0] = 1
ans = 0
while heap:
    val, r,c = heapq.heappop(heap)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and jido[r][c] > jido[nr][nc]:
            if not visited[nr][nc]:
                heapq.heappush(heap, (-jido[nr][nc], nr, nc))
            visited[nr][nc] += visited[r][c]


print(visited[n-1][m-1])

# ✅단순 BFS풀이로는 시간초과가 발생 why? BFS탐색으로 하면 이미 방문한 경로를 중복으로 탐색하게 돼. -> 그림으로 설명
# 때문에 최대힙과의 조합으로 중복을 없애주는 BFS + Heap으로 시간복잡도를 줄일 수 있다.
