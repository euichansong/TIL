"""
인접한 4칸, 3칸에 바다 있으면 없어진다
8방향 검사
"""
import sys
import copy

r, c = map(int, input().split())
nowmap = [list(input()) for _ in range(r)]
future = copy.deepcopy(nowmap)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 지형 변화
for i in range(r):
    for j in range(c):
        if nowmap[i][j] == 'X':  # 육지인 경우
            cnt = 0
            for p in range(4):
                nx = i + dx[p]
                ny = j + dy[p]
                # 바다이거나 맵을 벗어난 경우
                if not (0 <= nx < r and 0 <= ny < c) or nowmap[nx][ny] == '.':
                    cnt += 1
            if cnt >= 3:
                future[i][j] = '.'

# 모든 섬을 포함하는 직사각형 범위 계산
minga, maxga = r, -1
minse, maxse = c, -1

for i in range(r):
    for j in range(c):
        if future[i][j] == 'X':
            minga = min(minga, i)
            minse = min(minse, j)
            maxga = max(maxga, i)
            maxse = max(maxse, j)

# 최소 직사각형 출력
for ii in range(minga, maxga + 1):
    print(''.join(future[ii][minse:maxse + 1]))

