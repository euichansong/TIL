from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                q.append((i,j))

    while q:
        ti, tj = q.popleft()
        if matrix[ti][tj] != -1:
            for ni, nj in [[ti, tj+1],[ti+1, tj],[ti, tj-1],[ti-1, tj]]:
                if 0 <= ni < n and 0 <= nj < m:
                    if matrix[ni][nj] != -1 and matrix[ni][nj] ==0:
                        q.append((ni, nj))
                        matrix[ni][nj] = matrix[ti][tj] + 1


m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# bfs 함수 실행
bfs()
flag = True

for a in range(n):
    for b in range(m):
        if matrix[a][b] == 0:
            flag = False

maxx = 0
for a in range(n):
    for b in range(m):
        if maxx < matrix[a][b]:
            maxx = matrix[a][b]
if flag == False:
    print(-1)
else:
    print(maxx-1)