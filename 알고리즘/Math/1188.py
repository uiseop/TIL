import sys

input = sys.stdin.readline

N,M = map(int,input().split())
# 8 ,4 -> 4-1 : 3 
# M -> 3 , 3 , 3 - > 9  M-1 - (GCD - 1) : M - GCD

def GCD(a,b):
    if a % b == 0:
        return b
    return GCD(b, a%b)

print(M - GCD(N,M))