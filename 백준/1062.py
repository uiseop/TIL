def DFS(idx, cnt):
    global ans

    if cnt == k-5:
        readCnt = 0
        for word in words:
            check = True
            for w in word:
                if not alpha[ord(w) - ord("a")]:
                    check = False
                    break
            if check:
                readCnt += 1
        ans = max(ans, readCnt)
        return
    
    for i in range(idx, 26):
        if not alpha[i]:
            alpha[i] = True
            DFS(i, cnt + 1)
            alpha[i] = False

n,k = map(int,input().split())

if k < 5:
    print(0)
    exit()

elif k == 26:
    print(n)
    exit()

ans = 0
words = list(set(input()) for _ in range(n))
alpha = [0] * 26

for a in ["a","n","t","i","c"]:
    alpha[ord(a) - ord("a")] = 1

DFS(0,0)
print(ans)

