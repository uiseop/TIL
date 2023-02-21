import heapq
import sys
sys.setrecursionlimit(10**9)

# 하, 상, 우, 좌
# d, u, r, l
dr = [1,0,0,-1]
dc = [0,-1,1,0]
dir = ['d','l', 'r', 'u']

def solution(n, m, x, y, r, c, k):
    result = []
    answer = [['',[x-1,y-1]]]
    row,col = r-1, c-1
    # def dfs(visited, cur, target, routes, k, isTouched):
    def dfs():
        routes,[cur_r,cur_c] = heapq.heappop(answer)
        if len(routes) > k: return
        if abs(row - cur_r) + abs(col - cur_c) > k - len(routes): return
        if cur_r == row and cur_c == col:
            if len(routes) == k:
                result.append(routes)
                return 
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if  0 <= nr < n and 0 <= nc < m:
                heapq.heappush(answer, [routes + dir[i], [nr,nc]])
                dfs()
            # if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                # visited[nr][nc] = True
                # dfs(visited, [nr,nc], target, routes + [dir[i]], k, isTouched)
                # visited[nr][nc] = False
    
    dfs()
    # dfs(visited, [x-1,y-1], [r-1,c-1], [], k, False)
    return result[0] if result else "impossible"