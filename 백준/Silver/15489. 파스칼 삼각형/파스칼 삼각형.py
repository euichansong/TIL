"""
1
3
7
15
31

2의 제곱씩 늘어나는데 

이게 왜 dp야

"""
r,c,w = map(int,input().split())
dp = [[1] * i for i in range(1,32)]
for i in range(2,31):
    for j in range(1,len(dp[i]) -1):
        # 3,2 는 2,1 + 2,2 
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
# for i in dp:
#     print(i)
ans = 0
# r 부터 r + w 까지가 행의 범
for i in range(r-1,r-1+w):
    # c부터 c + (i-r) 까지 가 열의 범위
    for j in range(c-1, c-1 + (i-(r-1)) +1):
        ans+=dp[i][j]
print(ans)