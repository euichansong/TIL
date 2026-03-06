"""
2 초	192 MB

왼쪽위 시작 오른쪽 밑 끝
시작하는 칸과 끝나는 칸도 포함해서 센다.

벽마다 갈수있는 최단경로 저장 하고 그 점 시작점으로 하는 bfs 2번?
>> 시간초과 


>> visit에 플래그 넣는다? 
"""
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
mat = [list(input()) for _ in range(n)]
ans = 1e9
# 시작점, 벽깼는지여부, 칸갯수
def bfs(si, sj):
    global ans
    visit = [[[0]*2 for _ in range(m)]for _ in range(n)]
    visit[si][sj][0] = 1
    q = deque()
    # 시작점,플래그
    q.append([si, sj, 0])
    while q:
        tx,ty,flag = q.popleft()
        if tx == n-1 and ty == m-1:
            # print(visit[tx][ty][0],visit[tx][ty][1],ans)
            ans = min(ans,visit[tx][ty][flag])
            return
        for nx,ny in ([tx,ty+1],[tx+1,ty],[tx,ty-1],[tx-1,ty]):
            # 방문안한곳
            if 0 <=nx<n and 0<=ny< m and visit[nx][ny][flag] == 0:
                # 방문한곳 0인경우
                if mat[nx][ny] == '0' and visit[nx][ny][flag] == 0:
                    visit[nx][ny][flag] = visit[tx][ty][flag]+1
                    q.append([nx,ny,flag])
                
                # 방문한곳 1인경우
                elif mat[nx][ny] == '1' and flag == 0:
                    # 부순적 없으면 부시기
                    if visit[nx][ny][1] == 0:
                        visit[nx][ny][1] = visit[tx][ty][flag]+1
                        q.append([nx,ny,1])
bfs(0,0)

if ans == 1e9:
    print(-1)
else:
    print(ans)


# 시간초과 코드  벽마다 갈수있는 최단경로 저장 하고 그 점 시작점으로 하는 bfs 2번?
# # 시작점, 벽깼는지여부, 칸갯수
# def bfs(si, sj, flag, cnt):
#     global ans
#     if cnt > ans:
#         return
#     visit = [[0]*m for _ in range(n)]
#     visit[si][sj] = 1
#     q = deque()
#     q.append([si, sj, cnt])
#     while q:
#         tx, ty, dis = q.popleft()
#         if tx == n - 1 and ty == m - 1:
#             ans = min(ans, dis)
#             return
#         for nx,ny in ([tx,ty+1],[tx+1,ty],[tx,ty-1],[tx-1,ty]):
#             # 방문안한곳
#             if 0 <=nx<n and 0<=ny< m and visit[nx][ny] == 0:
#                 # 방문한곳 0인경우
#                 if mat[nx][ny] == '0':
#                     visit[nx][ny] = 1
#                     q.append([nx, ny, dis+1])
#                 # 방문한곳 1인경우
#                 elif mat[nx][ny] == '1':
#                     # 벽 안부시면 부시고 체크
#                     if not flag:
#                         bfs(nx,ny,True,dis+1)
#                         visit[nx][ny] = 1

# bfs(0,0,False,1)

# if ans == 1e9:
#     print(-1)
# else:
#     print(ans)




