import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
board = list(list(map(int,input().split())) for _ in range(n))

if n == 1:
    print(board[0][0])
    exit()

def top(bd):
    board = deepcopy(bd)
    max_value = 0
    happed = [[False for _ in range(n)] for _ in range(n)]
    for r in range(1,n):
        for c in range(n):
            row = r
            col = c
            while board[row][col] != 0 and 1 <= row < n and not happed[row-1][col] and not happed[row][col]:
                if board[row-1][col] == 0:
                    board[row-1][col] += board[row][col]
                    board[row][col] = 0
                elif board[row-1][col] == board[row][col]:
                    happed[row-1][col] = True
                    board[row-1][col] += board[row][col]
                    board[row][col] = 0
                max_value = max(max_value, board[row-1][col])
                row -= 1
    return board, max_value

def down(bd):
    board = deepcopy(bd)
    max_value = 0
    happed = [[False for _ in range(n)] for _ in range(n)]
    for r in range(n-1,-1,-1):
        for c in range(n):
            row = r
            col = c
            while board[row][col] != 0 and 0 <= row < n-1 and not happed[row+1][col] and not happed[row][col]:
                if board[row+1][col] == 0:
                    board[row+1][col] += board[row][col]
                    board[row][col] = 0
                elif board[row+1][col] == board[row][col]:
                    happed[row+1][col] = True
                    board[row+1][col] += board[row][col]
                    board[row][col] = 0
                max_value = max(max_value, board[row+1][col])
                row += 1
    return board, max_value


def right(bd):
    board = deepcopy(bd)
    max_value = 0
    happed = [[False for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n-1,-1,-1):
            row = r
            col = c
            while board[row][col] != 0 and 0 <= col < n-1 and not happed[row][col+1] and not happed[row][col]:
                if board[row][col+1] == 0:
                    board[row][col+1] += board[row][col]
                    board[row][col] = 0
                elif board[row][col+1] == board[row][col]:
                    happed[row][col+1] = True
                    board[row][col+1] += board[row][col]
                    board[row][col] = 0
                max_value = max(max_value, board[row][col+1])
                col += 1
    return board, max_value

def left(bd):
    board = deepcopy(bd)
    max_value = 0
    happed = [[False for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(1,n):
            row = r
            col = c
            while board[row][col] != 0 and 1 <= col < n and not happed[row][col-1] and not happed[row][col]:
                if board[row][col-1] == 0:
                    board[row][col-1] += board[row][col]
                    board[row][col] = 0
                elif board[row][col-1] == board[row][col]:
                    happed[row][col-1] = True
                    board[row][col-1] += board[row][col]
                    board[row][col] = 0
                max_value = max(max_value, board[row][col-1])
                col -= 1
    return board, max_value

def dfs(funcs, cnt):
    board, value = funcs
    if cnt == 5:
        return value
    value = max(value, dfs(top(board), cnt+1), dfs(down(board), cnt+1), dfs(left(board), cnt+1), dfs(right(board), cnt+1))
    return value


answer = max(dfs(top(board), 1), dfs(down(board), 1), dfs(left(board), 1), dfs(right(board), 1))

print(answer)

