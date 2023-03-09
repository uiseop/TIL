import math
import sys

input = sys.stdin.readline

n = int(input())

def numToStirng(n):
    return str(n)

def is_prime_number(x):
    if x == 1: return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


while True:
    num = numToStirng(n)
    left = 0
    right = len(num) - 1

    while left < right:
        if num[left] == num[right]:
            left += 1
            right -= 1
        else: break

    if left >= right and is_prime_number(n):
        print(n)
        exit()
    n += 1

