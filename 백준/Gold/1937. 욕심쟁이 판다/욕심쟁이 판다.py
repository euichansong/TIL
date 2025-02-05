import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
bam = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(sx, sy):
    if dp[sx][sy] != 0: 
        return dp[sx][sy]
    
    dp[sx][sy] = 1
    for fx, fy in dir:
        nx, ny = sx + fx, sy + fy
        if 0 <= nx < n and 0 <= ny < n and bam[nx][ny] > bam[sx][sy]:
            dp[sx][sy] = max(dp[sx][sy], dfs(nx, ny) + 1)
    
    return dp[sx][sy]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)
