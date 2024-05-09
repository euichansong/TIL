n = int(input())
winelist = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)

dp[1] = winelist[1]
if n > 1:
    dp[2] = winelist[1] + winelist[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + winelist[i], dp[i-3] + winelist[i-1] + winelist[i])

print(dp[n])