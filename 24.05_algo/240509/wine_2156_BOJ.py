"""
1번은
2번 경우의수 2번 고른 경우, 1번 2번 고른 경우

3번 경우의수 3번 1번 3번 고른 경우 , 2번 3번 고른 경우  123은 안된다
음수 없으니 3번부터 시작은 배재

4번 경우의 수 13 4 12 4

6
100
100
0
0
100
100
"""
n = int(input())
winelist = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)

dp[1] = winelist[1]
if n > 1:
    dp[2] = winelist[1] + winelist[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + winelist[i], dp[i-3] + winelist[i-1] + winelist[i])

print(dp[n])