import sys

input = sys.stdin.readline
valid = 'valid'
invalid = 'invalid'

def isGameEnd(arr, w):
    if arr[0][0]==arr[0][1]==arr[0][2]==w:
        return True
    if arr[1][0]==arr[1][1]==arr[1][2]==w:
        return True
    if arr[2][0]==arr[2][1]==arr[2][2]==w:
        return True
    if arr[0][0]==arr[1][0]==arr[2][0]==w:
        return True
    if arr[0][1]==arr[1][1]==arr[2][1]==w:
        return True
    if arr[0][2]==arr[1][2]==arr[2][2]==w:
        return True
    if arr[0][0]==arr[1][1]==arr[2][2]==w:
        return True
    if arr[2][0]==arr[1][1]==arr[0][2]==w:
        return True
    return False

while True:
    cmd = input().rstrip()
    if cmd == 'end':
        break
    
    arr = list(cmd)
    arr_2d = [[None for _ in range(3)] for _ in range(3)]

    XCnt = arr.count('X')
    OCnt = arr.count('O')
    if XCnt == OCnt + 1 or XCnt == OCnt:
    
        for i in range(9):
            row = i // 3
            col = i % 3
            arr_2d[row][col] = arr[i]

        XBingo = isGameEnd(arr_2d, 'X')
        OBingo = isGameEnd(arr_2d, 'O')
        
        if XCnt == OCnt and not XBingo and OBingo:
            print(valid)
            continue
        if XCnt == OCnt + 1 and XBingo and not OBingo:
            print(valid)
            continue
        if XCnt + OCnt == 9 and not OBingo:
            print(valid)
            continue
        print(invalid)
    else:
        print(invalid)