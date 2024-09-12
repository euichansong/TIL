from collections import deque


def solution(maps):
    answer = 0
    # n m 은 서로 다른 값일 수도 있다
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        startx, starty = q.popleft()
        for i in range(4):
            nx = startx + dx[i]
            ny = starty + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                if visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[startx][starty] + 1
    if visited[n - 1][m - 1] == 0:
        answer = -1
    else:
        answer = visited[n - 1][m - 1]

    return answer