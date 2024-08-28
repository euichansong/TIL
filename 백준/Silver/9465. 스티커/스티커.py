import sys
input = sys.stdin.readline
t = int(input())
for tt in range(t):
    n = int(input())
    fir = list(map(int, input().split()))
    sec = list(map(int, input().split()))
    dp = [[0]*n for _ in range(2)]
    # print(fir,sec)
    """
    fir[0]골랐으면 sec[1] 고르는 경우 or sec[1]+fir[2] or sec[2]
    sec[0]골랐으면 fir[1] or sec[2]
    
    대각선, 한칸 건너뛰고 큰값 구하는 경우
    """
    if n == 1:
        print(max(fir[0], sec[0]))
        continue
        
    dp[0][0] = fir[0]
    dp[1][0] = sec[0]

    dp[0][1] = sec[0] + fir[1]
    dp[1][1] = fir[0] + sec[1]

    for i in range(2,n):
        # sec 0 시작
        dp[0][i] += max(dp[1][i-1], dp[1][i-2]) + fir[i]
        # fir 0 시작
        dp[1][i] += max(dp[0][i-1], dp[0][i-2]) + sec[i]
    print(max(dp[0][-1],dp[1][-1]))