"""
6
10
20
15
25
10
20
"""
n = int(input())
pointlist = [0] + [int(input()) for _ in range(n)] + [0]
# dp값, 카운트
dp = [[0,0] for _ in range(n+2)]

# 0은 다음칸 갈 수 있다
# 1은 다음칸으로 못간다 무조건 2칸 뛰어야 함
dp[1][0] = pointlist[1]
# 처음 1,1은 0이지만 10으로 표기
dp[1][1] = pointlist[1]
dp[2][0] = pointlist[2]
dp[2][1] = dp[1][0] + pointlist[2]

for i in range(3,n+1):
    dp[i][0] = max(dp[i-2][1], dp[i-2][0]) + pointlist[i]
    dp[i][1] = dp[i-1][0] + pointlist[i]

print(dp)
print(max(dp[n]))


