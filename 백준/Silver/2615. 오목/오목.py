"""
6알 이상 은 아님
"""
pan = [list(map(int, input().split())) for _ in range(19)]
# 하, 우하, 우상, 우
dx = [1, 1, -1, 0]
dy = [0, 1, 1, 1]

def five():
    for i in range(19):
        for j in range(19):
            if pan[i][j] != 0: 
                color = pan[i][j]
                for p in range(4): 
                    cnt = 1
                    for g in range(1, 6):
                        nx = i + dx[p] * g
                        ny = j + dy[p] * g
                        if 0 <= nx < 19 and 0 <= ny < 19 and pan[nx][ny] == color:
                            cnt += 1
                        else:
                            break
                    
                    # 이전칸과 다음칸 확인
                    px = i - dx[p]
                    py = j - dy[p]
                    nnx = i + dx[p] * 5
                    nny = j + dy[p] * 5

                    if cnt == 5:
                        if not (0 <= px < 19 and 0 <= py < 19 and pan[px][py] == color):
                            if not (0 <= nnx < 19 and 0 <= nny < 19 and pan[nnx][nny] == color):
                                return color, i + 1, j + 1 
    return 0, -1, -1

ans, ans_i, ans_j = five()
print(ans)
if ans != 0:
    print(ans_i, ans_j)



