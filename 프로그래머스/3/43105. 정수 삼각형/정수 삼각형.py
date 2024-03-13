def solution(triangle):
    n = len(triangle)
    triangle[1][0] = triangle[1][0] + triangle[0][0]
    triangle[1][1] = triangle[1][1] + triangle[0][0]
    for i in range(2,n):
        triangle[i][0] = triangle[i-1][0] + triangle[i][0]
        triangle[i][-1] = triangle[i-1][-1] + triangle[i][-1]
        for j in range(1,i):
            a = triangle[i-1][j-1]
            b = triangle[i-1][j]
            triangle[i][j] = max(a,b) + triangle[i][j]
    answer = max(triangle[n-1])
    return answer