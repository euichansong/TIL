di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]
def bfs(i, j, matrix):
    q = []
    q.append((i, j))
    matrix[i][j] = '0'
    while q:
        i, j = q.pop(0)
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < h and 0 <= nj < w and matrix[ni][nj] == '1':
                q.append((ni, nj))
                matrix[ni][nj] = '0'

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        cnt = 0
        matrix = [list(input().split()) for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == '1':
                    bfs(i,j,matrix)
                    cnt += 1
        print(cnt)