from collections import deque
import sys
input = sys.stdin.readline
dz = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dx = [0,0,0,0,1,-1]


def bfs():
    q = deque()
    for aa in range(z):
        for bb in range(y):
            for cc in range(x):
                if matrix[aa][bb][cc] == 1:
                    q.append((aa, bb, cc))
    while q:
        tz, ty, tx = q.popleft()
        if matrix[tz][ty][tx] != -1:
            for w in range(6):
                nz = tz + dz[w]
                ny = ty + dy[w]
                nx = tx + dx[w]
                if 0 <= nz < z and 0 <= ny < y and 0 <= nx < x:
                    if matrix[nz][ny][nx] == 0:
                        matrix[nz][ny][nx] = matrix[tz][ty][tx] + 1
                        q.append((nz, ny, nx))


x, y, z = map(int, input().split())

# 3차원 배열
matrix = [[list(map(int, input().split())) for _ in range(y)] for _ in range(z)]
# bfs 함수 실행
bfs()
# 0이 나오면 토마토가 다 안익는 다는 뜻
# 맥스값 찾기 == 최소 일수 찾는것
flag = True
maxx = 0
for a in range(z):
    for b in range(y):
        for c in range(x):
            if matrix[a][b][c] == 0:
                flag = False
            if maxx < matrix[a][b][c]:
                maxx = matrix[a][b][c]
if flag == False:
    print(-1)
else:
    print(maxx-1)