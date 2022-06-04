from collections import deque
import sys

input = sys.stdin.readline

def bfs(n):
    q = deque([n])
    visited[n][0] = 0
    visited[n][1] = 1

    while q:
        pos = q.popleft()

        for i in [pos-1, pos+1, pos*2]:
            if 0 <= i <= 100000:
                if visited[i][0] == -1: # 처음 도달한다면
                    visited[i][0] = visited[pos][0] + 1 # 도달할 때 까지 걸린 시간 저장
                    visited[i][1] = visited[pos][1] # 경우의 수 저장
                    q.append(i)
                
                elif visited[i][0] == visited[pos][0] + 1: # 도달하는 최단 시간이 같으면
                    visited[i][1] += visited[pos][1]

n,k = map(int,input().split())

visited = [[-1,0] for _ in range(100001)]

bfs(n)
print(visited[k][0])
print(visited[k][1])