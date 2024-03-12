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
# print(pointlist)
dp = [[0,0] for _ in range(n+2)]
# print(dp)
dp[1][0] = pointlist[1]
dp[1][1] = pointlist[1]
dp[2][0] = pointlist[2]
dp[2][1] = dp[1][0] + pointlist[2]
# # dp[2] = max(pointlist[1], dp[1] + pointlist[2])
# print("=======")
# print(dp)
# print(dp[1])
# print(dp[3])
# print("=======")
for i in range(3,n+1):
    dp[i][0] = max(dp[i-2][1], dp[i-2][0]) + pointlist[i]
    dp[i][1] = dp[i-1][0] + pointlist[i]
    # print(dp[i][0])
    # print(dp[i][1])
    # print(dp)
    # print("----------")
print(max(dp[n]))
    # if (dp[i - 2][0] + pointlist[i - 1]) > (dp[i-1][0] + pointlist[i]):
    #     pass
    # elif (dp[i - 2][0] + pointlist[i - 1]) < (dp[i-1][0] + pointlist[i]):
    #     pass
    # elif (dp[i - 2][0] + pointlist[i - 1]) == (dp[i-1][0] + pointlist[i]):
    #     pass
#print(dp)

