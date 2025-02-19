import sys
input = sys.stdin.readline

from collections import deque

n,m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] *m for _ in range(n)]

for i in range(n):
    for j in range(m):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + maze[i][j]

print(dp[n-1][m-1])
