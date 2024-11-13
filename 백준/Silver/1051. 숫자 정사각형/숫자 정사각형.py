"""
50이니까 for문 난사 가능
꼭지점이니까 점 기준 우 하 대각 보면 될듯
"""

n,m = map(int, input().split())
mtx = [list(input()) for _ in range(n)]
nmm = min(n,m)
di = [1,0,1]
dj = [0,1,1]
ans = 1
for i in range(n):
    for j in range(m):
        for ne in range(nmm):
            lx = i + di[0]*ne
            ly = j + dj[0]*ne
            dx = i + di[1]*ne
            dy = j + dj[1]*ne
            rx = i + di[2]*ne
            ry = j + dj[2]*ne
            if 0<= lx < n and 0<= ly < m and 0<= dx < n and 0<= dy < m and 0<= rx < n and 0<= ry < m:
                if mtx[i][j] == mtx[lx][ly] and mtx[i][j] == mtx[dx][dy] and mtx[i][j] == mtx[rx][ry]:
                    ans = max(ans,((ne+1)*(ne+1)))
print(ans)

