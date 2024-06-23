"""
점화식을 어떻게 구하지?
1번 케이스
1일 [0,0,0,10,0,0,0,0]
2일 [0,0,0,0,0,0,20,0]
3일 [0,0,0,10,0,0,0,0]
4일 [0,0,0,10,10+20,0,0,0]
5일 [0,0,0,10,30,0,30+15,0,0]
"""
import sys
input = sys.stdin.readline

n = int(input())
daylist = [[0,0]]+[list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

# for i in range(1, n+1):
#     dp[i] = max(dp[i], dp[i-1])
#     if i + daylist[i][0] < n+1:
#         dp[i + daylist[i][0]] = max(dp[i+daylist[i][0]], dp[i] + daylist[i][1])
# print(dp)

for i in range(1, n+1):
    dp[i] = max(dp[i], dp[i-1])
    # i-1해야  1일차 상담하면 4일차 상담 가능
    newi = i-1 + daylist[i][0]
    newp = daylist[i][1]
    # 회사에 없으면 상담이 안된다
    if newi < n+1:
        dp[newi] = max(dp[newi], dp[i-1] + newp)
    print(dp)
print(max(dp))

