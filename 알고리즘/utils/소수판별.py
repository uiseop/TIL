def isPrimsNumber(n):
    arr = [True for _ in range(n+1)]
    arr[0] = False
    arr[1] = False

    for i in range(2, n+1):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i*j] = False
                j += 1
    
    result = []
    for i in range(n+1):
        if arr[i]:
            result.append(i)

    return result # 0~n까지의 소수를 리턴해준다