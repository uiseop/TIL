import sys

input = sys.stdin.readline

n,m,R = map(int,input().split())

A = list(list(map(int,input().split())) for _ in range(n))

def calculate():
    width = m
    height = n
    for i in range(min(n,m) // 2):
        rotate(i,i, width, height)
        width -= 2
        height -= 2
    for a in A:
        print(*a)

def rotate(row,col, width, height):
    length = 2*(width-1) + 2*(height-1)
    rows = []
    for c in range(col, col+width):
        rows.append(A[row][c])
    
    for r in range(row+1, row+height):
        rows.append(A[r][col+width-1])
    
    for c in range(col+width-2, col-1, -1):
        rows.append(A[row+height-1][c])
    
    for r in range(row+height-2, row, -1):
        rows.append(A[r][col])
    
    r_rows = [0 for _ in range(length)]
    for i in range(length):
        rid = i - (R % length)
        r_rows[rid] = rows[i]
    rid = 0
    for c in range(col, col+width):
        A[row][c] = r_rows[rid]
        rid += 1
    for r in range(row+1, row+height):
        A[r][col+width-1] = r_rows[rid]
        rid += 1
    
    for c in range(col+width-2, col-1, -1):
        A[row+height-1][c] = r_rows[rid]
        rid += 1
    
    for r in range(row+height-2, row, -1):
        A[r][col] = r_rows[rid]
        rid += 1
    return

calculate()