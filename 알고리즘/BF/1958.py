strings = list(input() for _ in range(3))

s1 = strings[0]
s2 = strings[1]
s3 = strings[2]

l1 = len(s1)
l2 = len(s2)
l3 = len(s3)

dp = list(list([0 for _ in range(l3+1)] for _ in range(l2+1)) for _ in range(l1+1))

for i in range(1,l1+1):
  for j in range(1, l2+1):
    for k in range(1, l3+1):
      if s1[i-1] == s2[j-1] and s2[j-1] == s3[k-1]:
        dp[i][j][k] = dp[i-1][j-1][k-1] + 1
      else:
        dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[-1][-1][-1])