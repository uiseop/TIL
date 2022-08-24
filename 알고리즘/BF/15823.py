from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

temp_max = n // m

cards = list(map(int,input().split()))

def find(num, visited):
    cnt = 0
    q = deque()
    index = 0
    while index < len(cards):
        if visited[cards[index]]:
            visited[q.popleft()] = False
            continue

        visited[cards[index]] = True
        q.append(cards[index])
        index += 1
        if len(q) == num:
            cnt += 1
            while q:
                visited[q.popleft()] = False
    return cnt

def b_search(n,m):
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        visited = [False for _ in range(500001)]
        t = find(mid, visited)
        if t < m:
            right = mid - 1
        else:
            left = mid + 1
    
    return right


print(b_search(n,m))