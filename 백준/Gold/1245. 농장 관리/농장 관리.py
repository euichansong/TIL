"""
2 초	128 MB

산봉우리는 같은 높이를 가지는 하나의 격자 혹은 인접한 격자들의 집합으로 이루어져 있다. 
(여기서 "인접하다"의 정의는 X좌표 차이와 Y좌표 차이 모두 1 이하일 경우로 정의된다.) 
또한 산봉우리와 인접한 격자는 모두 산봉우리의 높이보다 작아야한다.
"""
from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]

def bfs(sx,sy):
    q = deque()
    q.append([sx,sy])
    visit[sx][sy] = 1
    flag = True
    height = mat[sx][sy]
    while q:
        tx,ty = q.popleft()
        for i,j in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            nx = tx+i
            ny = ty+j
            if 0<= nx < n and 0<= ny < m:
                # 현재 높이보다 높으면 산봉우리가 아님
                if mat[nx][ny] > height:
                    flag = False

                if visit[nx][ny] == 0 and mat[nx][ny] == height:
                    q.append([nx,ny])
                    visit[nx][ny] = 1
    return flag

ans = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] != 0 and visit[i][j] == 0:
            if bfs(i, j):
                ans += 1

print(ans)