from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n = int(input())
str_dic = defaultdict(int)

alpha = list(map(str, input().split()))
word = input()

for i in range(0, len(alpha), 2):
    str_dic[alpha[i]] = int(alpha[i+1])

length = sum(str_dic.values())
answer = 0

str_set = set()

def getReverse(word, a,b):
    return word[:a] + "".join(reversed(word[a:b])) + word[b:]

def makeString(word, s, e):
    if s >= e-1:
        str_set.add(word)
        return
    
    length = s + e
    mid = length // 2
    
    # 왼쪽 거꾸로
    makeString(getReverse(word, s, mid), mid, e)
    # 오른쪽 거꾸러ㅗ
    makeString(getReverse(word, mid, e), s, mid)

    if length % 2 == 1:
        mid += 1
        makeString(getReverse(word, s, mid), mid ,e)
        makeString(getReverse(word, mid, e), s, mid)

for i in range(len(word) - length):
    s_word = word[i:i+length]
    counter = Counter(s_word)
    for key in counter.keys():
        if counter[key] != str_dic[key]:
            break
    else:
        makeString(s_word,0,len(s_word))

print(len(str_set))