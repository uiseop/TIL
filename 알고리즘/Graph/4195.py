import sys
from collections import defaultdict

input = sys.stdin.readline

def union(parents, i, j):
    pi = find(parents, i)
    pj = find(parents, j)
    if pi < pj:
        parents[pi][1] += parents[pj][1]
        parents[pj] = parents[pi]
    else:
        parents[pj][1] += parents[pi][1]
        parents[pi] = parents[pj]
    return

def find(parents, i):
    if parents[i][0] == i:
        return i
    parent = parents[i][0]
    n_parent = find(parents, parent)
    return n_parent


for _ in range(int(input())):
    F = int(input())
    parents = [[i,1] for i in range(100000 * 2 + 1)]
    
    f_dict = defaultdict(int)
    f_num = 1
    for _ in range(F):
        f1, f2 = map(str, input().split())
        
        if f_dict[f1] == 0:
            f_dict[f1] = f_num
            f_num += 1
        if f_dict[f2] == 0:
            f_dict[f2] = f_num
            f_num += 1
        i = f_dict[f1]
        j = f_dict[f2]
        if find(parents, i) != find(parents, j):
            union(parents, i, j)
        print(parents[find(parents, i)][1])