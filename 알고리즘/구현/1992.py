n = int(input())

video = list(list(input()) for _ in range(n))

bies = [2**i for i in range(7)]

n_lim = 0

for i in range(len(bies)):
    if bies[i] == n:
        n_lim = i
        break

def getQuadTree(row,col, bid):
    root = video[row][col]
    for i in range(bies[bid]):
        r = row + i
        for j in range(bies[bid]):
            c = col + j
            if root == video[r][c]: continue
            break
        else: continue
        break
    else:
        return str(root)
    
    
    res = ''
    for dr,dc in [[0,0], [0,bies[bid-1]],[bies[bid-1],0], [bies[bid-1],bies[bid-1]]]:
        res += getQuadTree(row+dr, col+dc, bid-1)
    return '(' + res + ')'

print(getQuadTree(0,0,n_lim))
