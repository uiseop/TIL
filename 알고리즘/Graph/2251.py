import sys

input = sys.stdin.readline

A,B,C = map(int,input().split())

volume = set()

visited = [[False for _ in range(B+1)] for _ in range(A+1)]


def water(a,b):
    if not visited[a][b]:
        visited[a][b] = True
        c = C - a - b
        if a == 0:
            volume.add(c)
        
        if a > 0 and b < B: # a에서 b로 물을 따름
            w = min(a, B-b)
            water(a-w, b+w)
        
        if a > 0 and c < C: # a에서 c로 물을 따름
            w = min(a, C-c)
            water(a-w, b)
        
        if b > 0 and a < A: # b에서 a로
            w = min(b, A-a)
            water(a+w, b-w)

        if b > 0 and c < C: # b에서 c로
            w = min(b, C-c)
            water(a, b-w)

        if c > 0 and a < A: # c에서 a로
            w = min(c, A-a)
            water(a+w, b)

        if c > 0 and b < B: # c에서 b로
            w = min(c, B-b)
            water(a, b+w)

water(0,0)

s_volume = sorted(list(volume))

for i in s_volume:
    print(i, end=" ")


            
