import sys

input = sys.stdin.readline

n = int(input())

s = n // 5

strs = list(input().rstrip())

dot_nums = [
    [[0,1], [0,2], [1,0], [1,2], [2,0], [2,2], [3,0], [3,2], [4,0], [4,1], [4,2]],
    [[1,0], [2,0], [3,0], [4,0]],
    [[0,1], [0,2], [1,2], [2,0], [2,2], [3,0], [4,0], [4,1], [4,2]],
    [[0,1], [0,2], [1,2], [2,0], [2,1], [2,2], [3,2], [4,0], [4,1], [4,2]],
    [[0,2], [1,0], [1,2], [2,0], [2,1], [2,2], [3,2], [4,2]],
    [[0,1], [0,2], [1,0], [2,0], [2,1], [2,2], [3,2], [4,0], [4,1], [4,2]],
    [[0,1], [0,2], [1,0], [2,0], [2,1], [2,2], [3,0], [3,2], [4,0], [4,1], [4,2]],
    [[0,1], [0,2], [1,2], [2,2], [3,2], [4,2]],
    [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1], [2,2], [3,0], [3,2], [4,0], [4,1], [4,2]],
    [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1], [2,2], [3,2], [4,0], [4,1], [4,2]]
]

signals = [[0 for _ in range(s)] for _ in range(5)]

i = 0
for r in range(5):
    for c in range(s):
        signals[r][c] = 1 if strs[i] == '#' else 0
        i += 1

c = 0
r = 0
answer = ''
while c != s:
    if signals[0][c] != 1:
        c += 1
        continue
    num = 0
    dot_count = 0
    for nums in range(10):
        count = 0
        for dr,dc in dot_nums[nums]:
            if r + dr < 5 and c + dc < s and signals[r + dr][c + dc]:
                count += 1
                continue
            else: break
        else:
            if count > dot_count:
                dot_count = count
                num = nums

    c += max(dot_nums[num], key=lambda x: x[1])[1] + 1
    answer += str(num)

print(answer)

