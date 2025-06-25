"""
1 초	128 MB
"""
t = int(input())
for _ in range(t):
    n = int(input())
    won = list(map(int, input().split()))
    need = int(input())
    # 금액별 가짓수
    dp = [[0] * (need+1) for _ in range(n+1)]
    # 0 만드는 가지수는 무조건 1
    for i in range(n+1):
        dp[i][0] = 1

    # 가능한 동전 
    for i in range(n):
        # 모든 금액
        for j in range(1,need+1):
            # 동전 안쓰면 이전 누적 가져오기
            dp[i][j] = dp[i-1][j]
            # 지금 동전 사용하는 경우
            # 이전 값+동전 이니까  이전 누적값 + 가능한 경우의수
            if j >= won[i]:
                dp[i][j] += dp[i][j-won[i]]

    print(dp[n-1][need])