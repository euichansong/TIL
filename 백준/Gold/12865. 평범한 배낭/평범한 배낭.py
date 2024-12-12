import sys
input = sys.stdin.readline
n,k = map(int, input().split())
item = [[0,0]]+ [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]
# 물품
for i in range(1,n+1):
    # 무게
    for j in range(1,k+1):
        gram = item[i][0]
        val = item[i][1]
        # 무게를 넘치게 가질경우 이전물품의 최대값
        if j < gram:
            dp[i][j] = dp[i-1][j]
        else:
            # 이전 최대값, 이전값에서 무게 뺀값 + 이번 물품의 가치
            dp[i][j] = max(dp[i-1][j], dp[i-1][j -gram] + val)

print(dp[n][k])

