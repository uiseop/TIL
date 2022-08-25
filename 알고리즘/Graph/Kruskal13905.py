import sys

input = sys.stdin.readline

def get_parent(parent, x):
    if parent[x] != x:
        parent[x] = get_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def answer(arr):
    for h1, h2, k in arr:
        union_parent(parent, h1, h2)
        if get_parent(parent, s) == get_parent(parent, e):
            return k
    return 0


# 집의 수, 다리의 수
N, M = map(int, input.split())
# 시작, 끝
s, e = map(int, input.split())

parent = [x for x in range(N+1)]

# m 개의 줄에는 다리의 정보
arr = [tuple(map(int, input.split())) for _ in range(M)]
arr.sort(key=lambda x: -x[2])

print(answer(arr))