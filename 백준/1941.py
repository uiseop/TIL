import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def dfs(arr,s,y):
    global ans
    if s + y == 7:
        if s >= 4:
            arr.sort()
            ans.add(tuple(arr))
            return True
        return False
    if y >= 4:
        return False
    
    adjacent = []
    # ✅키 포인트. 한붓 긋기가 아니라, 백트랙킹으로 돌아갈 수 있도록 인접한 모든 경로를 추가해준다.
    # 백트랙킹 방식을 사용. 
    for r,c in arr:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < 5) and (0 <= nc < 5) and not visited[nr][nc]:
                adjacent.append((nr,nc))
    
    for r,c in adjacent:
        visited[r][c] = 1
        if room[r][c] == "S":
            dfs(arr + [(r,c)], s+1,y)
        else:
            dfs(arr + [(r,c)], s,y+1)
        visited[r][c] = 0

room = list(list(input()) for _ in range(5))

ans = set()

for row in range(5):
    for col in range(5):
        visited = [[0 for _ in range(5)] for _ in range(5)]
        visited[row][col] = 1
        if room[row][col] == "S":
            dfs([(row,col)],1,0)
        else:
            dfs([(row,col)],0,1)

print(len(ans))