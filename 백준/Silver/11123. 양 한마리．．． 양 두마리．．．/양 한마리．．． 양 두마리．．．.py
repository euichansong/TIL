di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
def bfs(i, j, matrix):
    q = []
    q.append((i, j))
    matrix[i][j] = '.'
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < h and 0 <= nj < w and matrix[ni][nj] == '#':
                q.append((ni, nj))
                matrix[ni][nj] = '.'

t = int(input())

for tc in range(1, t+1):
    h, w = map(int, input().split())
    matrix = [list(input()) for _ in range(h)]
    cnt = 0
    for q in range(h):
        for e in range(w):
            if matrix[q][e] == '#':
                bfs(q, e, matrix)
                # print(matrix)
                cnt += 1
    print(cnt)