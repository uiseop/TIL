def makeTemp(r,c,num):
    for i in range(n):
        nr = r + i
        nc = c + i
        if 0 <= nr < n and 0 <= nc < n:
            temp[nr][nc] += num
        nc = c - i
        if 0 <= nr < n and 0 <= nc < n:
            temp[nr][nc] += num
        nr = r - i
        if 0 <= nr < n and 0 <= nc < n:
            temp[nr][nc] += num
        nc = c + i
        if 0 <= nr < n and 0 <= nc < n:
            temp[nr][nc] += num

def check(r,c):
    if temp[r][c]:
        return False
    return True


def DFS(idx, cnt):
    global ans

    if idx >= len(ones):
        ans = max(ans,cnt)
        return

    r,c = ones[idx]

    if check(r,c):
        makeTemp(r,c,1)
        DFS(idx + 1, cnt + 1)
        # 다시 지우고, 해당 좌표 선택 안하고 넘어가버리기
        makeTemp(r,c,-1)
        DFS(idx + 1, cnt)
    else:
        DFS(idx + 1, cnt)
                        
            
                

n = int(input())

chess = [list(map(int,input().split())) for _ in range(n)]

ones = []
for i in range(n):
    for j in range(n):
        if chess[i][j] == 1:
            if (i + j) % 2 == 0:  # 짝수는 백색 칸
                ones.append([i,j])

ans = 0
temp = [[0 for _ in range(n)] for _ in range(n)]
DFS(0,0)
res1 = ans

ones = []
for i in range(n):
    for j in range(n):
        if chess[i][j] == 1:
            if (i+j) % 2 == 1:
                ones.append([i,j])

ans = 0
temp = [[0 for _ in range(n)] for _ in range(n)]
DFS(0,0)
res2 = ans
print(res1 + res2)

# ✅체스판 문제의 특이점 파악하는것이 중요하다.
# 체스판에서의 비숍은 대각선으로밖에 움직이지 못함.
# 하지만 이 대각선은 현재 밟고있는 색 들과 같은 색뿐만 밟을 수 있음.
# 때문에 흰색에 있는 비숍은 절대로 검정색에 있는 비숍을 잡지 못해.
# 그러므로 흰색과 검정색의 좌표를 나눠서 탐색 => 탐색범위를 반으로 줄일 수 있슴. 굿.