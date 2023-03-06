import sys

input = sys.stdin.readline

N,M = map(int,input().split())

A = list(list(map(int,input().split())) for _ in range(N))

r_min = 0
c_min = 0

test = [col for col in zip(A)]
for a in zip(*A):
    print(a)

cntArray = [[1 for _ in range(M)] for _ in range(N)]
for r in range(N):
    for c in range(M):
        if r == 0 and c == 0 or r == 0 and c == M-1 or r == N-1 and c == 0 or r == N-1 and c == M-1:
            continue
        if 0 < r < N-1 and 0 < c < M-1:
            cntArray[r][c] = 4
        else:
            cntArray[r][c] = 2

originSum = sum(A[r][c] * cntArray[r][c] for r in range(N) for c in range(M))

for row in [0, N-1]:
    r_min = max(r_min, A[row][0] + A[row][M-1] + sum(A[row][1:M-1]) * 2)

for col in [0, M-1]:
    c_min = max(c_min, A[0][col] + A[N-1][col] + sum(A[r][col] for r in range(1,N-1)) * 2)

def getColSum(array, col):
    result = 0
    for r in range(1,N-1):
        result += array[r][col]
    return result

minSum = min(A[row][0] + A[row][M-1] + 2 * sum(A[row][1:M-1]) for row in range(1,N-1))
result = max(originSum, originSum - minSum + r_min)
minSum = min(A[0][col] + A[N-1][col] + 2 * getColSum(A, col) for col in range(1,M-1))
print(max(result, originSum - minSum + c_min))
