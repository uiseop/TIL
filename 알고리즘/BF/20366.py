import sys

input = sys.stdin.readline

n = int(input())

snows = list(map(int,input().split()))

snows.sort()

answer = float("inf")

for i in range(n-3):
    for j in range(i+3, n):
        left = i+1
        right = j-1

        while left < right:
            anna = snows[i] + snows[j]
            elsa = snows[left] + snows[right]
            result = anna - elsa

            answer = min(answer, abs(result))

            if result < 0:
                right -= 1
            else:
                left += 1

print(answer)