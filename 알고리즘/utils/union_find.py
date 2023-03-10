def union(a,b):
    pA = find(a)
    pB = find(b)
    if pA < pB:
        parents[pB] = pA
    else:
        parents[pA] = pB

def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a]) # 경로 압축을 사용한 방법
    return parents[a]

    return find(parents[a]) # 경로 압축을 사용하지 않고, 선형적으로 탐색하는 방법


parents = [i for i in range(n)]