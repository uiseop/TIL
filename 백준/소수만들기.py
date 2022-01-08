n = int(input())

# 0~2n까지의 소수를 확인할 배열을 선언합니다.
prime = [True] * (2*n+1)
prime[0] = prime[1] = False

# 2 이상의 수에 대해 소수인지 확인합니다.
for i in range(2, 2*n+1) :
    if not prime[i] :

        continue
    
    # 2i~(i-1)i는 2~(i-1)의 배수를 제외할 때 제거되었기 때문에 고려하지 않습니다.
    for j in range(i*i, 2*n+1, i) :
        prime[j] = False


ans = 0
for i in range(n+1, 2*n+1) :
    if prime[i] :
        ans += 1

print(ans)