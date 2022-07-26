import sys
sys.setrecursionlimit(30000)

FF, FS, SF, SS = map(int, input().split())

ans = float('-inf')
ch = dict()
def DFS(level, cur, FF, FS, SF, SS):
    global ans, ch
    a = str(cur)+str(FF)+str(FS)+str(SF)+str(SS)
    if a in ch:
        return
    else:
        ch[a] = 1
        
    ans = max(ans, level)
    # FF, FS 1개 이상 있을 때
    if level==0 and cur==-1:
        if FF >= 1:
            DFS(1, 'FF', FF-1, FS, SF, SS)
        if FS >= 1:
            DFS(1, 'FS', FF, FS-1, SF, SS)
        return
    if level==0 and cur==-2:
        if SF >= 1:
            DFS(1, 'SF', FF, FS, SF-1, SS)
        if SS >= 1:
            DFS(1, 'SS', FF, FS, SF, SS-1)
        return

    if cur == 'FF' or cur=='SF':
        if FF >= 1:
            DFS(level+FF, 'FF', 0, FS, SF, SS)
        if FS >= 1:
            DFS(level+1, 'FS', FF, FS-1, SF, SS)
    if cur == 'SS' or cur=='FS':
        if SS >= 1:
            DFS(level+SS, 'SS', FF, FS, SF, 0)
        if SF >= 1:
            DFS(level+1, 'SF', FF, FS, SF-1, SS)

if FF or FS:        
    DFS(0, -1, FF, FS, SF, SS)
else:
    DFS(0, -2, FF, FS, SF, SS)

print(ans)