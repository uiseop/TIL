import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))  # 배열 데이터
sum_dict = {0: 1}  # 누적합 관련 dict
sum_val = 0  # 누적합
answer = 0  # 합이 K인 부분합의 개수
for i in arr:
    sum_val += i
    if sum_val - k in sum_dict.keys():  # 현재까지의 누적합에서 k를 뺀 값이 sum_dict에 있다면 
        answer += sum_dict[sum_val - k]  # answer에 해당하는 값의 value만큼 더하기

    # sum_dict에 현재까지의 누적합에 해당하는 value 값에 1 더해주기
    if sum_val in sum_dict.keys():
        sum_dict[sum_val] += 1
    else:
        sum_dict[sum_val] = 1
print(answer)