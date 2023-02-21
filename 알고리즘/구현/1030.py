import sys

input = sys.stdin.readline

s,n,k,r1,r2,c1,c2 = map(int,input().split())

def getFractal(time, row, col):
    if time == 0:
        return '0'

    if time == 1:
        br1 = (n-k) // 2
        br2End = br1 + k
    else:
        br1 = 3**(time-2)*n
        br2End = br1*2
    

    if br1 <= row < br2End and br1 <= col < br2End:
        return '1'
    else:
        width = n * 3**(time-2)
        return getFractal(time-1, row % width, col % width)

result = []

for row in range(r1,r2+1):
    rows = ''
    for col in range(c1, c2+1):
        rows += getFractal(s, row, col)
    result.append(rows)

print('\n'.join(result))
