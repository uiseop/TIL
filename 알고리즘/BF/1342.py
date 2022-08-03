from collections import Counter

S = list(input())

counter = Counter(S)

ks = counter.keys()

if len(ks) == len(S):
    total = 1
    for i in range(2, len(S)+1):
        total *= i
    print(total)
    exit()

ans = 0


def dfs(cnt, w):
    global ans

    if cnt == len(S):
        ans += 1
        return
        
    for k in ks:
        if counter[k] == 0:
            continue

        if w and w[-1] == k: 
            continue
        
        counter[k] -= 1
        dfs(cnt+1, w + k)
        counter[k] += 1


dfs(0,'')
print(ans)