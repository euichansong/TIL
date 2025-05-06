"""
2 초	512 MB

2중 bfs?
"""
from collections import deque
import sys
input = sys.stdin.readline

n,l,r = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

def bfs(sx,sy):
    q = deque()
    q.append([sx,sy])
    visit[sx][sy] = 1
    union = deque()
    union.append([sx,sy])
    total = mat[sx][sy]
    while q:
        tx,ty = q.popleft()
        for x,y in [[1,0],[-1,0],[0,1],[0,-1]]:
            nx = tx+x
            ny = ty+y
            # 국경선 여는 조건
            if 0<= nx < n and 0<= ny < n and visit[nx][ny] == 0 and l <= abs(mat[nx][ny]-mat[tx][ty]) <= r:
                q.append([nx,ny])
                union.append([nx,ny])
                total += mat[nx][ny]
                visit[nx][ny] = 1

    if len(union) > 1:
        for ux,uy in union:
            mat[ux][uy] = total // len(union)
        return True
    else:
        return False

answer = 0

while True:
    visit = [[0]*n for _ in range(n)]
    flag = True
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                if bfs(i, j):
                    flag = False

    if flag:
        print(answer)
        break

    answer += 1


