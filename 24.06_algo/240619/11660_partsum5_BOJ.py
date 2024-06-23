"""
# 시간 초과
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    answer = 0
    for i in range(x2-x1+1):
        for j in range(y2-y1+1):
            #print(x1+i,y1+j)
            answer += arr[x1+i][y1+j]
    print(answer)
# ====================================================
"""

"""
합을 다 구해놓고 dp 뽑아 쓰기?
라기엔 ;
줄 단위로 합 구하고 빼야할듯?
2중 for 문 사용시 쿼리당 O(n) 시간이 걸리기 때문에 전체 시간 복잡도는 O(n * m)
전체 누적합 구해서 더하고 뺀다
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

# dp 누적
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = arr[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 총 누적에서 밑에줄 옆에줄 겹치는 거 더해주기 >> 2차원 배열 누적합 구하는 공식
    answer = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(answer)
