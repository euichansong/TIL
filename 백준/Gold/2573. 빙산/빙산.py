"""
풍선팡 bfs 2개 같이 사용 하기
"""
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]

def bfs(starti, startj, visited):
    q = deque()
    q.append([starti,startj])
    visited[starti][startj] = 1
    while q:
        pi, pj = q.popleft()
        for ni, nj in [[pi+1,pj],[pi,pj+1],[pi-1,pj],[pi,pj-1]]:
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and iceberg[ni][nj] != 0:
                q.append([ni,nj])
                visited[ni][nj] = visited[pi][pj] + 1


# 남,동,북,서
di = [1,0,-1,0]
dj = [0,1,0,-1]
answer = 0

while True:

    for i in range(n):
        for j in range(m):
            if iceberg[i][j] != 0:
                nearsea = 0
                for p in range(4):
                    ni = i + di[p]
                    nj = j + dj[p]
                    if 0 <= ni < n and 0 <= nj < m and iceberg[ni][nj] == 0:
                        nearsea += 1
                iceberg[i][j] -= nearsea
                # 0으로 바꾸면 다음칸에 영향 가니까 -1로 변경
                if iceberg[i][j] <= 0:
                    iceberg[i][j] = -1
    # 1년에 녹은거 0으로 변경
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] == -1:
                iceberg[i][j] = 0
    # 덩어리 갯수 찾는 bfs
    mass = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            # 빙산이 있는데 방문 안했으면 덩어리 찾기
            if iceberg[i][j] != 0 and visited[i][j] == 0:
                bfs(i,j,visited)
                mass += 1
    # print("visited")
    # for i in range(n):
    #     print(visited[i])
    # for i in range(n):
    #     print(iceberg[i])
    # print("덩어리",mass)
    answer += 1
    if mass >= 2:
        print(answer)
        break
    if mass == 0:
        print(0)
        break