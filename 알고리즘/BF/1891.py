import sys

input = sys.stdin.readline

d, num = map(str,input().split())
x,y = map(int,input().split())

r = 0
c = 0

def find_coordinate(i,row,col):
    global r,c
    if i == int(d):
        r = row
        c = col
        return
    pos = num[i]

    if pos == '1':
        find_coordinate(i+1, row*2, col*2 + 1)
    elif pos == '2':
        find_coordinate(i+1, row*2, col*2)
    elif pos == '3':
        find_coordinate(i+1, row*2 + 1, col*2)
    else:
        find_coordinate(i+1, row*2 + 1, col*2 + 1)

def get_position(r,c,n):
    answer = ''
    while n != 0:
        n -= 1
        if 0 <= r < 2**n and 0 <= c < 2**n:
            answer += '2'
        elif 0 <= r < 2**n and 2**n <= c < 2**(n+1):
            answer += '1'
            c -= 2**n
        elif 2**n <= r < 2**(n+1) and 0 <= c < 2**n:
            answer += '3'
            r -= 2**n
        else:
            answer += '4'
            r -= 2**n
            c -= 2**n
    return print(int(answer))

find_coordinate(0,0,0)

r -= y
c += x

if 0 <= r < 2**int(d) and 0 <= c < 2**int(d):
    get_position(r,c,int(d))
else:
    print(-1)