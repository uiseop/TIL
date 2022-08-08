n,m = map(int,input().split())

p1 = [['0' for _ in range(150)] for _ in range(150)]

for i in range(n):
    lst = list(input())
    for j in range(m):
        p1[50+i][50+j] = lst[j]

N,M = map(int,input().split())

p2 = list(list(input()) for _ in range(N))

holes = 0
for i in range(n):
    for j in range(m):
        if p1[i][j] == '0':
            holes += 1

def getOnse(arr):
    ret = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == '1':
                ret.append([i,j])
    return ret

deg90 = list(zip(*p2[::-1]))
deg180 = list(zip(*deg90[::-1]))
deg270 = list(zip(*deg180[::-1]))

p2s = [p2, deg90, deg180, deg270]

def isInRage(lt,lb,rt,rb, offset):
    for i in range(2):
        lt[i] += offset
        lb[i] += offset
        rt[i] += offset

for p in p2s:
    lt, rb = [0, 0], [len(p) - 1, len(p[0]) - 1]
    lb, rt = [rb[0], 0], [0, rb[1]]
    offset = [1,1]
    while sum(offset) < 200:
        if isInRage(lt,lb,rt,rb, offset):

