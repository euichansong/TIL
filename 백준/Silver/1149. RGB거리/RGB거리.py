"""
첫번째 최소값
두번째 최소값
세번째 최소값 은 필요 없지 않을까 두번째랑 알아서 다르면 상관 없을듯
상관 있을듯
1. 첫번째 0 인 경우
    2-1. 2번째 1인경우
        2-1-1. 3번째 2, 0 인 경우
    2-2. 2번째 2인경우
         2-2-1. 3번째 1,0 인 경우
=> 1. 첫번째 0인 경우
    2. 2번째 0이 아닌 경우

"""

n = int(input())
# pricelist[n][0] = Red / pricelist[n][1] = Green / pricelist[n][2] = Blue
pricelist = [[0,0,0]]+ [list(map(int, input().split())) for _ in range(n)]
dp = [[0,0,0] for _ in range(n+1)]
# print(pricelist)
# print(dp)
for i in range(1, n+1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + pricelist[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + pricelist[i][1]
    dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + pricelist[i][2]
print(min(dp[n]))
