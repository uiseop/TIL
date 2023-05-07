import sys

input = sys.stdin.readline

n,m = map(int,input().split())

words = []

curLength = 0

for i in range(n):
    word = input().rstrip()
    curLength += len(word)
    words.append(word)

left = m - curLength

minCount = left // (n-1)
maxBar = left % (n-1)
minBar = n - 1 -maxBar

s = '_' * minCount

result = [words[0]]

for i in range(1,n):
    if words[i][0] > 'Z':
      if maxBar:
        result.append(s + '_')
        maxBar -= 1
      elif minBar:
        result.append(s)
        minBar -= 1
    else:
      if minBar:
        result.append(s)
        minBar -= 1
      elif maxBar:
        result.append(s+'_')
        maxBar -= 1
    result.append(words[i])
  

for s in result:
    print(s, end='')
