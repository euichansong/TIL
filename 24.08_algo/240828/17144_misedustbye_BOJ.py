import sys
input = sys.stdin.readline
r,c,t = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
cleaner = []
# 1. 확산
def hwak():
    # 임시 배열 사용
    temp_matrix = [[0] * c for _ in range(r)]
    temp_matrix[cleaner[0][0]][0] = -1
    temp_matrix[cleaner[1][0]][0] = -1

    for i in range(r):
        for j in range(c):
            if matrix[i][j] > 0:
                spread_amount = matrix[i][j] // 5
                spread_count = 0
                for p in range(4):
                    nx = i + dx[p]
                    ny = j + dy[p]
                    if 0 <= nx < r and 0 <= ny < c and matrix[nx][ny] != -1:
                        temp_matrix[nx][ny] += spread_amount
                        spread_count += 1
                temp_matrix[i][j] += matrix[i][j] - spread_amount * spread_count

    for i in range(r):
        for j in range(c):
            matrix[i][j] = temp_matrix[i][j]
# 이 방식으로 하면 틀리다 순차 업데이트에 문제가 생긴다
# def hwak():
#     dustlist = []
#     for i in range(r):
#         for j in range(c):
#             if matrix[i][j] != 0 and matrix[i][j] != -1:
#                 dustlist.append([i,j])
#     for ii,jj in dustlist:
#         cnt = 0
#         spray = matrix[ii][jj] // 5
#         for p in range(4):
#             nx = dx[p] + ii
#             ny = dy[p] + jj
#             if 0 <= nx < r and 0 <= ny < c and matrix[nx][ny] != -1:
#                 matrix[nx][ny] += spray
#                 cnt += 1
#         matrix[ii][jj] -= spray * cnt

# 위 공청기 순환 (역으로 계산)
def upcycle():
    si = cleaner[0][0]
    # 왼쪽 벽
    for i in range(si - 1, 0, -1):
        matrix[i][0] = matrix[i - 1][0]
    # 천장
    for j in range(c - 1):
        matrix[0][j] = matrix[0][j + 1]
    # 오른쪽 벽
    for i in range(si):
        matrix[i][c - 1] = matrix[i + 1][c - 1]
    # 바닥
    for j in range(c - 1, 1, -1):
        matrix[si][j] = matrix[si][j - 1]
    # 공기청정기 바로 옆
    matrix[si][1] = 0


# 아래 공청기 순환 (역으로 계산)
def downcycle():
    si = cleaner[1][0]
    # 왼쪽 벽
    for i in range(si + 1, r - 1):
        matrix[i][0] = matrix[i + 1][0]
    # 바닥
    for j in range(c - 1):
        matrix[r - 1][j] = matrix[r - 1][j + 1]
    # 오른쪽 벽
    for i in range(r - 1, si, -1):
        matrix[i][c - 1] = matrix[i - 1][c - 1]
    # 천장
    for j in range(c - 1, 1, -1):
        matrix[si][j] = matrix[si][j - 1]
    # 공기청정기 바로 옆
    matrix[si][1] = 0

# 공청기 위치 찾기
for i in range(r):
    if matrix[i][0] == -1:
        cleaner.append([i,0])

# 함수 실행
for _ in range(t):
    hwak()
    # for q in range(r):
    #     print(matrix[q])
    # print("=====================")
    upcycle()
    downcycle()

#총합 계산
answer = 0
for i in range(r):
    for j in range(c):
        if matrix[i][j] != -1 and matrix[i][j] != 0:
            answer += matrix[i][j]

print(answer)