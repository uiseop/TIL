


def solution(commands):
    result = []
    answer = [[None for _ in range(51)] for _ in range(51)]
    parents = [[0 for _ in range(51)] for _ in range(51)]
    for i in range(51):
        for j in range(51):
            parents[i][j] = [i,j]

    def union(r1,c1,r2,c2):
        pr1, pc1 = find(r1,c1)
        pr2, pc2 = find(r2,c2)
        parents[pr2][pc2] = [pr1, pc1]
        updatePos(pr2, pc2, answer[r1][c1])
    
    def find(r,c):
        if parents[r][c][0] == r and parents[r][c][1] == c:
            return [r,c]
        
        pr,pc = find(parents[r][c][0], parents[r][c][1])
        parents[r][c] = [pr, pc]
        return [pr, pc]
    
    def ununion(r,c):
        pr,pc = find(r,c)
        temp = answer[pr][pc]
        for row in range(51):
            for col in range(51):
                if parents[row][col][0] == pr and parents[row][col][1] == pc:
                    parents[row][col] = [row,col]
                    answer[row][col] = None
        answer[r][c] = temp
        return

    
    def updatePos(r,c,val):
        pr,pc = find(r,c)
        for r in range(51):
            for c in range(51):
                tr,tc = find(r,c)
                if pr == tr and pc == tc:
                    answer[r][c] = val
    
    def updateVal(v1,v2):
        for r in range(51):
            for c in range(51):
                if answer[r][c] == v1:
                    answer[r][c] = v2
    
    for command in commands:
        cmd_arr = ''.join(command).split(' ')
        print(cmd_arr, 'haha')
        if cmd_arr[0] == 'UPDATE':
            if len(cmd_arr) == 4:
                cmd, r,c, val = cmd_arr
                r,c = int(r), int(c)
                updatePos(r,c,val)
            else:
                cmd, val1, val2 = cmd_arr
                updateVal(val1, val2)
        elif cmd_arr[0] == 'MERGE':
            cmd, r1,c1, r2,c2 = cmd_arr
            r1,c1, r2,c2 = int(r1), int(c1), int(r2), int(c2)
            if answer[r1][c1] and answer[r2][c2]:
                union(r1,c1, r2,c2)
            elif answer[r2][c2]:
                union(r2,c2, r1,c1)
            else:
                union(r1,c1, r2,c2)
        elif cmd_arr[0] == 'PRINT':
            cmd, r,c = cmd_arr
            r,c = int(r), int(c)
            pr,pc = find(r,c)
            if answer[pr][pc]:
                result.append(answer[pr][pc])
            else:
                result.append('EMPTY')
        elif cmd_arr[0] == 'UNMERGE':
            cmd,r,c = cmd_arr
            r,c = int(r), int(c)
            ununion(r,c)

    return result

solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"])