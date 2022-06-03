import copy
from itertools import combinations
import heapq
from os import remove
import sys

input = sys.stdin.readline

n,m,d = map(int,input().split())

def find_enemy(pan, archer, removes):
    heap = []
    for r in range(n-1,-1,-1):
        for c in range(m):
            if pan[r][c] == 1:
                diff = abs(archer[0]-r) + abs(archer[1]-c)
                if diff <= d:
                    heapq.heappush(heap,[diff, c, r]) # diff, col, row 순으로 우선 순위 정렬
            
    if heap:
        # print(heap)
        _, col, row = heapq.heappop(heap)
        # print("killed", row,col)
        # pan[row][col] = 0
        removes.add((row,col))

def get_enemy_count(pan):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if pan[i][j] == 1: cnt += 1
    
    return cnt

def move_enemy(pan):
    pan[-1] = [0 for _ in range(m)]

    for i in range(-1, -n, -1):
        pan[i] = pan[i-1]
    
    pan[0] = [0 for _ in range(m)]

pan = list(list(map(int,input().split())) for _ in range(n))

castle = [i for i in range(m)]

l_archer = list(combinations(castle, 3))

answer = 0

for archers in l_archer:
    cnt = 0
    copy_pan = copy.deepcopy(pan)
    removes = set()
    while get_enemy_count(copy_pan):
        for col in archers:
            find_enemy(copy_pan, [n, col], removes)
        while removes:
            r,c = removes.pop()
            copy_pan[r][c] = 0
            cnt += 1
        move_enemy(copy_pan)

    answer = max(answer, cnt)

print(answer)