pan = [list(map(int, input().split())) for _ in range(19)]
# 방향: 하, 우하, 우상, 우
dx = [1, 1, -1, 0]
dy = [0, 1, 1, 1]

def five():
    for i in range(19):
        for j in range(19):
            if pan[i][j] != 0:  # 바둑알이 있는 경우만 탐색
                color = pan[i][j]
                for p in range(4):  # 4방향 탐색
                    cnt = 1
                    for g in range(1, 6):  # 최대 5칸 탐색
                        nx = i + dx[p] * g
                        ny = j + dy[p] * g
                        if 0 <= nx < 19 and 0 <= ny < 19 and pan[nx][ny] == color:
                            cnt += 1
                        else:
                            break
                    
                    # 이전칸과 다음칸 확인
                    prev_x = i - dx[p]
                    prev_y = j - dy[p]
                    next_x = i + dx[p] * 5
                    next_y = j + dy[p] * 5

                    if cnt == 5:
                        if not (0 <= prev_x < 19 and 0 <= prev_y < 19 and pan[prev_x][prev_y] == color):
                            if not (0 <= next_x < 19 and 0 <= next_y < 19 and pan[next_x][next_y] == color):
                                return color, i + 1, j + 1  # 1-based index
    return 0, -1, -1

# 결과 출력
ans, ans_i, ans_j = five()
print(ans)
if ans != 0:
    print(ans_i, ans_j)
