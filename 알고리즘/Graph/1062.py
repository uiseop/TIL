# import sys
# 1656 ms

# input = sys.stdin.readline

# def DFS(idx, cnt):
#     global ans

#     if cnt == k-5:
#         readCnt = 0
#         for word in words:
#             check = True
#             for w in word:
#                 if not alpha[ord(w) - ord("a")]:
#                     check = False
#                     break
#             if check:
#                 readCnt += 1
#         ans = max(ans, readCnt)
#         return
    
#     for i in range(idx, 26):
#         if not alpha[i]:
#             alpha[i] = True
#             DFS(i, cnt + 1)
#             alpha[i] = False

# n,k = map(int,input().split())

# if k < 5:
#     print(0)
#     exit()

# elif k == 26:
#     print(n)
#     exit()

# ans = 0
# words = list(set(input().rstrip()) for _ in range(n))
# alpha = [0] * 26

# for a in ["a","n","t","i","c"]:
#     alpha[ord(a) - ord("a")] = 1

# DFS(0,0)
# print(ans)


# 280 ms
import sys
from itertools import combinations
 
input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
words = [0] * N
base = ['a', 'n', 't', 'i', 'c']
for i in range(N):
    word = list(input())[4:-4]
    for ch in word:
        words[i] |= (1 << ord(ch) - ord('a'))
        
answer = 0
if K < 5:
    pass
else:
    alpha = 'bdefghjklmopqrsuvwxyz'
    append_case = list(combinations(list(alpha), K-5))
    for case in append_case:
        make_bit = 0
        for ch in base:
            make_bit |= (1 << ord(ch) - ord('a'))
        for ch in case:
            make_bit |= (1 << ord(ch) - ord('a'))
 
        count = 0
        for i in range(len(words)):
            if words[i] & make_bit == words[i]:
                count += 1
        
        answer = max(answer, count)
        
print(answer)