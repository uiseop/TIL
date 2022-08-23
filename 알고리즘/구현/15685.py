import sys

input = sys.stdin.readline

dir = [(0,1), (-1,0), (0,-1), (1,0)] # 동 북 서 남

def get_next_curve(arr):
    curve = []
    r,c,d = arr[-1]
    d = (d + 1) % 4
    r,c = r + dir[d][0], c + dir[d][1]
    curve.append((r,c,d))
    for i in range(len(arr) - 2):
        d = (arr[-i-2][2] + 1) % 4
        r,c = curve[i][0] + dir[d][0], curve[i][1] + dir[d][1]
        curve.append((r,c,d))
    return arr + curve

n = int(input())

points = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    col,row,d,g = map(int,input().split())
    arr = [(row,col,d), (row+dir[d][0], col+dir[d][1], d)]
    for _ in range(g):
        arr = get_next_curve(arr)
    
    for r,c,d in arr:
        if 0 <= r <= 100 and 0 <= c <= 100:
            points[r][c] = 1

ans = 0

for i in range(101):
    for j in range(101):
        if points[i][j]:
            for di,dj in [(1,0), (0,1), (1,1)]:
                if 0 <= i + di <= 100 and 0 <= j + dj <= 100 and points[i + di][j + dj]:  continue
                else: break
            else:
                ans += 1

print(ans)