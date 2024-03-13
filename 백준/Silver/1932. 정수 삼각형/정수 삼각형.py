def solution(triangle):
    n = len(triangle)
    if n >= 3:
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
    elif n == 2:
        triangle[1][0] = triangle[1][0] + triangle[0][0]
        triangle[1][1] = triangle[1][1] + triangle[0][0]
        answer = max(triangle[n - 1])
    else:
        answer = triangle[0][0]
    return answer

n = int(input())
first = int(input())
tri = [[] for _ in range(n)]
tri[0].append(first)
# print(tri)
for i in range(1,n):
    num = list(map(int, input().split()))
    tri[i] += num

print(solution(tri))