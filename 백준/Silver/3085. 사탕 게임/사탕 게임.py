"""
바꾼경우

상하좌우 다봐
좌 하 만 바꾸면 전체 다돌아도 괜찮다
"""

n = int(input())
board = [list(input()) for _ in range(n)]

dx = [0,1]
dy = [1,0]

answer = 1
for i in range(n):
    for j in range(n):
        # 좌 하 만 바꾼다
        for p in range(2):
            ni = dx[p] + i
            nj = dy[p] + j
            if 0 <= ni < n and 0 <= nj < n:
                # 교환
                board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
                for x in range(n):
                    # 가로
                    gacnt = 1
                    for y in range(1, n):
                        if board[x][y] == board[x][y - 1]:
                            gacnt += 1
                        else:
                            gacnt = 1
                        answer = max(answer, gacnt)

                    # 세로
                    secnt = 1
                    for y in range(1, n):
                        if board[y][x] == board[y - 1][x]:
                            secnt += 1
                        else:
                            secnt = 1
                        answer = max(answer, secnt)

                # 교환 복구
                board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
print(answer)
