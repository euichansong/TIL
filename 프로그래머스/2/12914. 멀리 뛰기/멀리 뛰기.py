def solution(n):
    answer = 0
    dp = [0] * (n+2) # 왜 n+1 하면 런타임 에러?
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+2):
        dp[i] = dp[i-1] + dp[i-2]
    answer = dp[n] % 1234567
    return answer