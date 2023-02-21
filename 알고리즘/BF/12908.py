from collections import deque
import heapq
import sys

input = sys.stdin.readline

def getDistance(x,y, tx,ty):
    return abs(abs(x)-abs(tx)) + abs(abs(y)-abs(ty))

xs, ys = map(int, input().split())
xe, ye = map(int, input().split())

teleport = []

for _ in range(3):
    tx, ty, ttx, tty = map(int,input().split())
    teleport.append([tx, ty])
    teleport.append([ttx, tty])

dq = []
heapq.heappush(dq, [getDistance(xs,ys, xe,ye), xs, ys, 0])

dx = [1,-1,0,0]
dy = [0,0,-1,1]


visited = [[xs,ys]]

while dq:
    dis, x,y, t = heapq.heappop(dq)
    print(x,y,t, dis)
    
    if x == xe and y == ye:
        print(t)
        break
    if [x,y] in teleport:
        idx = teleport.index([x,y])
        if idx % 2 == 0:
            nx, ny = teleport[idx+1]
            if getDistance(x,y, nx,ny) > 10:
                heapq.heappush(dq, [getDistance(nx,ny,xe,ye), nx, ny, t+10])
        else:
            nx, ny = teleport[idx-1]
            if getDistance(x,y, nx,ny) > 10:
                heapq.heappush(dq, [getDistance(nx,ny,xe,ye), nx, ny, t+10])

    cur = getDistance(x,y, xe, ye)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if [nx, ny] in visited  or nx < 0 or ny < 0 or nx > 10**9 or ny > 10**9:
            continue
        visited.append([nx, ny])
        heapq.heappush(dq, [getDistance(nx,ny,xe,ye), nx, ny, t+1])
