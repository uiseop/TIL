import sys

input = sys.stdin.readline

N, H, D = map(int,input().split())

rect = [list(input().rstrip()) for _ in range(N)]

def find_SEU(rect):
    us = set()

    for i in range(N):
        for j in range(N):
            if rect[i][j] != '.':
                if rect[i][j] == 'U':
                    us.add((i,j))
                elif rect[i][j] == 'S':
                    sr,sc = i,j
                elif rect[i][j] == 'E':
                    er,ec = i,j
    
    return sr,sc, er,ec, us


def solve(rect, N, H, D):
    sr,sc, er,ec, us = find_SEU(rect)
    result = [float('inf')]

    def dfs(r,c,h,u,t):
        d = abs(er-r) + abs(ec-c)
        if d <= h + u:
            result[0] = min(result[0], t+d)
        else:
            for i,j in list(us):
                d = abs(i-r) + abs(j-c)
                us.remove((i,j))
                if d <= h + u:
                    dfs(i,j,h-max(0, d-u-1), D-1, t+d)
                us.add((i,j))
    
    dfs(sr,sc,H,0,0)
    return -1 if result[0] == float('inf') else result[0]


print(solve(rect, N,H,D))