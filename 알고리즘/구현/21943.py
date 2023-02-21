from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

plus, mul = map(int,input().split())

op_list = [i for i in range(1,n)]

plus_index_combis = combinations(op_list, plus)

for combi in plus_index_combis:
    operations = ['*'] * n
    operations[0] = None

    for p in combi:
        operations[p] = '+'
    
    sentence = ''

    for i in range(n):
        if operations[i]:
            sentence += operations[i]
        sentence += str(nums[i])
    
    print(eval(sentence))