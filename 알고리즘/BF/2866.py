R,C = map(int,input().split())

words = list(input() for _ in range(R))

strs = ['' for _ in range(C)]
set_words = set()

for r in range(R-1, -1, -1):
    for c in range(C):
        strs[c] += words[r][c]
        set_words.add(strs[c])
    
    if len(set_words) == C:
        print(r)
        break
    set_words.clear()