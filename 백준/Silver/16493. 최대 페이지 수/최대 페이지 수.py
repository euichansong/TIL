import sys
input = sys.stdin.readline
n,m = map(int, input().split())
# 인덱스 방지용
day_page = [[0,0]]+ [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * (n + 1) for _ in range(m + 1)]

# 챕터
for i in range(1, m + 1):
    # 남은일 수
    for j in range(1, n + 1):
        day = day_page[i][0]
        page = day_page[i][1]

        # 현재 챕터의 수가 소요일수 보다 적으면 못읽음
        if j < day:
            dp[i][j] = dp[i - 1][j]
        else:
            # 이전 챕터의 최대 페이지, 이번 챕터 읽은 경우 
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - day] + page)

print(dp[m][n])
