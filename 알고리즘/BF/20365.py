import sys

input = sys.stdin.readline

s = int(input())

N = input()

B = 0
R = 0

pre = ''

if N[0] == 'B':
    B += 1
    pre = 'B'
else:
    R += 1
    pre = 'R'

for n in N[1:-1]:
    if n == pre:
        continue
    else:
        pre = n
        if n == 'B':
            B += 1
        else:
            R += 1
            
print(min(B,R) + 1)