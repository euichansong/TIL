"""
1 초	256 MB
"""
from collections import deque
import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline

r, c = map(int, input().split())

ma = [list(input().rstrip()) for _ in range(r)]
# 주변 막기
bor = ['O'] * (c + 2)
maze = []
maze.append(bor)
for row in ma:
    maze.append(['O'] + row + ['O'])
maze.append(bor)

# for rr in maze:
#     print(rr)



# 불 번짐
def fire():
    fl = []
    for i in range(r + 2):
        for j in range(c + 2):
            if maze[i][j] == 'F':
                fl.append([i, j])
    nfl = []
    for fi, fj in fl:
        for fx, fy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx = fi + fx
            ny = fj + fy
            if 0 <= nx < r + 2 and 0 <= ny < c + 2 and maze[nx][ny] == '.':
                nfl.append([nx, ny])

    for bx, by in nfl:
        maze[bx][by] = 'F'


# bfs
def bfs(sx, sy):
    global answer
    q = deque()
    visit = [[0] * (c + 2) for _ in range(r + 2)]
    q.append([sx, sy])
    visit[sx][sy] = 1
    while q:
        tx, ty = q.popleft()
        if maze[tx][ty] == 'O':
            return True
        if maze[tx][ty] != '.' or maze[tx][ty] != 'J':
            continue
        for fx, fy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx = tx + fx
            ny = ty + fy
            if 0 <= nx < r + 2 and 0 <= ny < c + 2 and maze[nx][ny] == '.':
                q.append([nx, ny])
                visit[nx][ny] = 1
        fire()
        answer += 1
    return False


# 시작점
def start():
    for i in range(r + 2):
        for j in range(c + 2):
            if maze[i][j] == 'J':
                aa = bfs(i, j)
                if aa:
                    print(answer)
                    return
                else:
                    print('IMPOSSIBLE')
                    return

answer = 0
start()
