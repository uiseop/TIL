from collections import deque
import sys

input = sys.stdin.readline

n,m,t = map(int,input().split())

pan = [None for _ in range(n+1)]

for i in range(n):
    lst = deque(list(map(int,input().split())))
    pan[i+1] = lst

def num2str(i,j):
    return str(i) + '.' + str(j)

def str2num(s):
    i,j = s.split('.')
    return [int(i),int(j)]

def getSum():
    ans = 0
    cnt = 0
    for i in range(1,n+1):
        for j in pan[i]:
            if str(type(j)) == "<class 'int'>":
                ans += j
                cnt += 1
    return [ans,cnt]

def Rotate(x,d,k):
    for i in range(1,n+1):
        if i % x == 0:
            if d == 0:
                pan[i].rotate(k)
            else:
                pan[i].rotate(-k)
    
    del_lst = set()
    for i in range(1,n+1):
        if i != n:
            for j in range(m):
                if pan[i][j] != 'x' and pan[i][j] == pan[i+1][j]:
                    del_lst.add(num2str(i,j))
                    del_lst.add(num2str(i+1,j))
        for j in range(m):
            if j != m-1:
                if pan[i][j] != 'x' and pan[i][j] == pan[i][j+1]:
                    del_lst.add(num2str(i,j))
                    del_lst.add(num2str(i,j+1))
            else:
                if pan[i][j] != 'x' and pan[i][j] == pan[i][0]:
                    del_lst.add(num2str(i,j))
                    del_lst.add(num2str(i,0))
    
    for s in del_lst:
        i,j = str2num(s)
        pan[i][j] = 'x'
    if not del_lst:
        tot, cnt = getSum()
        for i in range(1,n+1):
            for j in range(m):
                if str(type(pan[i][j])) == "<class 'int'>" and pan[i][j] > tot / cnt:
                    pan[i][j] -= 1
                elif str(type(pan[i][j])) == "<class 'int'>" and pan[i][j] < tot / cnt:
                    pan[i][j] += 1

for _ in range(t):
    x,d,k = map(int,input().split())
    Rotate(x,d,k)

print(getSum()[0])