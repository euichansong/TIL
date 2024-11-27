"""
같은칸 2번 방문 x
시작점과 끝점 2개가 무조건 존재한다
bfs 돌려서 2점 찾고 각각 명령어 갯수 비교해본다 이거 시간이 되나?

1부터 다음 홀수 번호까지 방향 찾기

4방향 비교해 숫자 나오면 [[0,2],[2,0],[0,-2],[-2,0]]: 해서 다음 홀수 찾기
"""
import sys

input = sys.stdin.readline
from collections import deque

h, w = map(int, input().split())
matrix = [list(input()) for _ in range(h)]
cnt = 0
for i in range(h):
    for j in range(w):
        if matrix[i][j] == '#':
            cnt += 1


def bfs(sx, sy):
    q = deque()
    visited = [[0] * w for _ in range(h)]
    q.append([sx, sy])
    visited[sx][sy] = 1
    while q:
        px, py = q.popleft()
        for fx, fy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx = px + fx
            ny = py + fy
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and matrix[nx][ny] == '#':
                q.append([nx, ny])
                visited[nx][ny] = visited[px][py] + 1
    max_visited = 0
    # for ii in range(h):
    #     print(visited[ii])
    # print("================")
    for ii in range(h):
        max_visited = max(max_visited, max(visited[ii]))
    return max_visited


def point_bfs(sx, sy):
    q = deque()
    visited = [[0] * w for _ in range(h)]
    q.append([sx, sy])
    visited[sx][sy] = 1
    while q:
        px, py = q.popleft()
        for fx, fy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx = px + fx
            ny = py + fy
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and matrix[nx][ny] == '#':
                q.append([nx, ny])
                visited[nx][ny] = visited[px][py] + 1
    for ii in range(h):
        print(visited[ii])
    print("================")
    return visited


point = []
for i in range(h):
    for j in range(w):
        if matrix[i][j] == '#':
            bcnt = bfs(i, j)
            if cnt == bcnt:
                # 시작점과 끝점
                point.append([i, j])

# 0,1,2,3은 북, 동, 남, 서
dx = [-2, 0, 2, 0]
dy = [0, 2, 0, -2]
f_di = -1


def find_road(sx, sy, vi, cnt):
    next_val = 3
    di = -1
    order = ''
    global f_di
    while next_val <= cnt:
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            # 처음 방향 정하기
            if f_di == -1 and 0 <= nx < h and 0 <= ny < w and vi[nx][ny] == 3:
                di = i
                f_di = i
            if 0 <= nx < h and 0 <= ny < w and vi[nx][ny] == next_val:
                if di == i:
                    next_val += 2
                    order += 'A'
                else:
                    # 우회전
                    if (di + 1) % 4 == i:
                        order += 'R'
                    # 좌회전
                    elif (di - 1) % 4 == i:
                        order += 'L'
                    di = i
                    next_val += 2
                    order += 'A'
                sx, sy = nx, ny
                break
    return order


# 4방향 비교해 숫자 나오면 [[0,2],[2,0],[0,-2],[-2,0]]: 해서 다음 홀수 찾기

vi = point_bfs(point[0][0], point[0][1])
o = find_road(point[0][0], point[0][1], vi, cnt)
print(point[0][0] + 1, point[0][1] + 1)
if f_di == 0:
    print('^')
elif f_di == 1:
    print('>')
elif f_di == 2:
    print('v')
elif f_di == 3:
    print('<')
print(o)

