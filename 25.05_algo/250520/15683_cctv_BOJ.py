"""
1 초	512 MB
cctv 8개, 회전 가능 최소 사각지대 > 백트
각각 cctv 돌려놓은 방향 다 구해서 가져다 쓰자
office는 가지고 다녀야해 > copy
"""
import sys, copy
sys.stdin = open("input.txt")
input = sys.stdin.readline


n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
answer = n * m + 1

# i,j, 카메라번호
cctv = []
for i in range(n):
    for j in range(m):
        if office[i][j] in [1, 2, 3, 4, 5]:
            cctv.append([i, j, office[i][j]])

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 회전 가능 방향
di = {
    1: [[0], [1], [2], [3]],
    2: [[2, 0], [3, 1]],
    3: [[3, 0], [0, 1], [1, 2], [2, 3]],
    4: [[2, 3, 0], [3, 0, 1], [0, 1, 2], [1, 2, 3]],
    5: [[0, 1, 2, 3]],
}


def back(now, matrix):
    global answer
    if now == len(cctv):
        spot = blind(matrix)
        answer = min(answer, spot)
        return
    # 현재 cctv 정보
    x, y, cctv_num = cctv[now]
    temp_office = copy.deepcopy(matrix)

    # [[0],[1],[2],[3]] 가 들어간다
    for direct in di[cctv_num]:
        # '#'으로 채우기
        change_sharp(x, y, direct, temp_office)
        # 다음 cctv
        back(now + 1, temp_office)
        # 돌기전 사무실
        temp_office = copy.deepcopy(matrix)


def change_sharp(x, y, direct, mat):
    for d in direct:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] != 6:
                if mat[nx][ny] == 0:
                    mat[nx][ny] = '#'
            else:
                break

# 사각지대 계산
def blind(mat):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                cnt += 1
    return cnt


back(0, office)
print(answer)
