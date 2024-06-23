n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

def path_recusion(matrix,i,j):
    if i == 0 or j == 0:
        return 0
    else:
        return matrix[i-1][j-1] + max(path_recusion(i-1, j), path_recusion(i, j-1))


def dynamic(matrix,n):
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,n+1):
            dp[i][j] = matrix[i-1][j-1] + max(dp[i-1][j], dp[i][j-1])


path_recusion(matrix,n,n)
dynamic(matrix,n)