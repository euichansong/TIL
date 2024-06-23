# from collections import deque
# r, c = map(int ,input().split())
# board = [list(input()) for _ in range(r)]
# # print(board)
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
#
# visited = deque([board[0][0]])
# answer = 1
# def BFS(starti,startj, cnt):
#     global answer
#     # if cnt < answer-1:
#     #     return
#     answer = max(cnt, answer)
#     # 4방향에서
#     for i in range(4):
#         nx = starti + dx[i]
#         ny = startj + dy[i]
#         # 범위 안벗어 나고
#         if 0 <= nx < r and 0 <= ny < c:
#             # 간적 없으면
#             if board[nx][ny] not in visited:
#                 visited.append(board[nx][ny])
#                 BFS(nx,ny, cnt +1)
#                 visited.pop()
#             # for j in visited:
#             #     if board[nx][ny] == j:
#             #         break
#             # visited.append(board[nx][ny])
#             # BFS(nx,ny, cnt +1)
#             # visited.pop()
# cnt = 1
# BFS(0,0,0)
# # print(visited)
# print(answer+1)

from collections import deque
r, c = map(int ,input().split())
board = [list(input()) for _ in range(r)]
# print(board)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

visited = deque([board[0][0]])
answer = 1
def BFS(starti,startj, cnt):
    global answer
    # if cnt < answer-1:
    #     return
    answer = max(cnt, answer)
    # 4방향에서
    for i in range(4):
        nx = starti + dx[i]
        ny = startj + dy[i]
        # 범위 안벗어 나고
        if 0 <= nx < r and 0 <= ny < c:
            # 간적 없으면
            if board[nx][ny] not in visited:
                visited.append(board[nx][ny])
                BFS(nx,ny, cnt +1)
                visited.pop()
            # for j in visited:
            #     if board[nx][ny] == j:
            #         break
            # visited.append(board[nx][ny])
            # BFS(nx,ny, cnt +1)
            # visited.pop()
cnt = 1
BFS(0,0,0)
# print(visited)
print(answer+1)