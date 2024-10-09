"""
bfs인데 백트?
k가 30 이하니까 재귀인데
k번만 나이트 처럼 이동
나이트는 장애물 뛰어넘음
나머진 인접 4방향
가장 큰 문제1. 언제 나이트처럼 이동?

1
4 2
0 0 1 0
0 0 1 0
어떻게 뛰어넘지?

k 포함한 visited 만들면?
"""
from collections import deque
# # 나이트
# kx = [-1, 1, 2,2,1,-1,-2,-2]
# ky = [-2,-2,-1,1,2, 2, 1,-1]
# # 우 하 좌 상
# dx=[1,0,-1,0]
# dy=[0,1,0,-1]

k = int(input())
w,h = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(h)]

startx,starty = 0,0
visited = [[[0] * (k+1) for _ in range(w)] for qqq in range(h)]

def bfs(startx,starty,startk):
    q = deque()
    q.append([startx,starty,startk])
    visited[startx][starty][startk] = 0
    while q:
        px,py,pk = q.popleft()
        if px == h-1 and py == w-1:
            return visited[px][py][pk]
        if pk > 0:
            for fx,fy in [[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1]]:
                nx = px + fx
                ny = py + fy
                if 0 <= nx < h and 0 <= ny < w and visited[nx][ny][pk-1] == 0 and array[nx][ny] == 0:
                    q.append([nx,ny,pk-1])
                    visited[nx][ny][pk-1] = visited[px][py][pk] + 1

        for fx,fy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx = px + fx
            ny = py + fy
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny][pk] == 0 and array[nx][ny] == 0:
                q.append([nx,ny,pk])
                visited[nx][ny][pk] = visited[px][py][pk] + 1     
    return -1

print(bfs(0,0,k))