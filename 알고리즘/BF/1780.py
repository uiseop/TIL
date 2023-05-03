import sys

input = sys.stdin.readline

n = int(input())

result = [0,0,0] # -1, 0, 1

arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))

def isAllSame(r,c,l):
    origin = arr[r][c]
    for i in range(l):
        for j in range(l):
            nr = r + i
            nc = c + j
            if arr[nr][nc] == origin:
                continue
            else:
                divides = divide_nine(r,c,l)
                for r,c,l in divides:
                    isAllSame(r,c,l)
                return
    
    if origin == -1:
        result[0] += 1
    elif origin == 0:
        result[1] += 1
    else:
        result[2] += 1
    return True

def divide_nine(r,c,l):
    lengths = [0, l//3, l//3 * 2]
    result = []
    for dr in lengths:
        for dc in lengths:
            result.append([r + dr, c + dc, l//3])
    return result

isAllSame(0,0,n)

for r in result:
    print(r)