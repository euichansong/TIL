"""
1 초	256 MB
(1 ≤ N ≤ 50, 1 ≤ M ≤ 10, 1 ≤ H ≤ 1,000)

10,007로 나눈 나머지? 엄청 많다는 뜻

이거 배낭이네
"""
n,m,h = map(int, input().split())
# 0 넣어줘야 계속 갱신 + 0 고르면 안골랐다는 뜻
block = [[0]+list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (h+1) for _ in range(n+1)]
dp[0][0] = 1
# 명수
for i in range(n):
    # 높이
    for j in range(h+1):
        # 블록
        for k in block[i]:
            if j+k <= h:
                # 현재 합산 높이 누적 = 이전 블록에서 만들수 있는 높이의 경우의수 누적 + 지금 고른 블록 합친 것 높이 누적
                dp[i+1][j+k] = dp[i][j] + dp[i+1][j+k]

print(dp[n][h] % 10007)
# for i in dp:
#     print(i)
        

