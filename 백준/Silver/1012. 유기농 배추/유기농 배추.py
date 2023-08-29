di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
def bfs(i, j, visited):
    q = []
    q.append((i,j))
    visited[i][j] = 0
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < m and 0 <= nj < n and visited[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = 0

t = int(input())

for tc in range(1, t+1):
    m, n, k = map(int, input().split())
    visited = [[0]*n for _ in range(m)]
    cnt = 0
    for _ in range(k):
        v1, v2 = map(int, input().split())
        visited[v1][v2] = 1
    for q in range(m):
        for e in range(n):
            if visited[q][e] == 1:
                bfs(q, e, visited)
                cnt += 1
    print(cnt)