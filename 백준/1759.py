l,c = map(int,input().split())
alpha = list(map(str,input().split()))

visited = [0] * c
alpha.sort()

def check(_string):
    mo = 0
    ja = 0
    for i in _string:
        if i in ["a","e","i","o","u"]:
            mo += 1
        else:
            ja += 1
    return mo, ja

def DFS(idx, length, string):
    if length == l:
        mo, ja = check(string)
        if mo >= 1 and ja >= 2:
            print("".join(string))
            
        return
    for i in range(c):
        if idx < i and not visited[i]:
            visited[i] = 1
            string.append(alpha[i])
            DFS(i, length + 1, string)
            visited[i] = 0
            string.pop()

DFS(-1, 0, [])