n = int(input())
dp = [0] * 1516
dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(3,n+1):
    if i % 2 == 0:
        dp[i] = dp[i-1] * 2 + 1
    else:
         dp[i] = dp[i-1] * 2 - 1

answer = dp[n] % 1000000007
print(answer)
