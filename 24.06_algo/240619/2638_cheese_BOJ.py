"""
치즈 옆 0이 가로세로 기준

2변 이상 접촉하는 경우 찾아서 좌표 값 넣는다

1인 경우 4변 보고 카운트해서 2를 넘으면 0으로 바꾼다
4변에서 0이 나온 경우 >> dx dy 의 가로 세로에 1이 없으면 줄이 하나라도 있으면 공기가 통한다

"""
from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]


def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if paper[nx][ny] >= 1:
                    paper[nx][ny] += 1
                else:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
answer = 0
while True:
    visited = [[0] * m for _ in range(n)]
    bfs()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if paper[i][j] >= 3:
                paper[i][j] = 0
                cnt += 1
            elif paper[i][j] == 2:
                paper[i][j] = 1
    if cnt > 0:
        answer += 1
    if cnt == 0:
        break
    for i in range(n):
        print(visited[i])
    print("=========================================")
print(answer)