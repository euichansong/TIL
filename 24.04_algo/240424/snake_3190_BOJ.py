"""
디큐써서 좌표값 넣기
popleft 써서 앞으로 땡기고 좌표값 바꿔서 append
"""
from collections import deque
n = int(input())
k = int(input())
board = [[0] * (n+1) for _ in range(n+1)]
for i in range(k):
    row,col = map(int, input().split())
    board[row][col] = 1
for j in board:
    print(j)
l = int(input())
movelist = list()
for i in range(l):
    x, c = input().split()
    x = int(x)
    movelist.append([x,c])

q = deque()
q.append((1,1))
finish=True
move = 0
# 1동,2남,3서,4북
direct = 1
next = 0
nextr, nextc = 1,1
eatapple = False
tailr, tailc = 0,0
while finish:
    nr, nc = q.popleft()
    if eatapple:
        nc = nextc
        nr = nextr
        board[tailr][tailc] = 0
    else:
        board[nr][nc] = 0
        nc = nextc
        nr = nextr
        tempc = nc
        tempr = nr
    if direct == 1 :
        nc += 1
        if nc == n:
            finish = False
        elif board[nr][nc] == -1:
            finish = False
    elif direct == 2:
        nr += 1
        if nr == n:
            finish = False
        elif board[nr][nc] == -1:
            finish = False
    elif direct == 3:
        nc -= 1
        if nc == 0:
            finish = False
        elif board[nr][nc] == -1:
            finish = False
    elif direct == 4:
        nr -= 1
        if nr == 0:
            finish = False
        elif board[nr][nc] == -1:
            finish = False
    if board[nr][nc] == 1:
        q.append((tempr, tempc))
        q.append((nr, nc))

        nextc = nc
        nextr = nr
        tailr, tailc = tempr, tempc
        eatapple = True
    else:
        nextc = nc
        nextr = nr
        q.append((nr, nc))
        board[tempr][tempc] = 0
        eatapple = False
    board[nr][nc] = -1

    move += 1
    if next >= l :
        continue
    elif move == movelist[next][0]:
        if movelist[next][1] == 'D':
            if direct == 4:
                direct = 1
            else:
                direct += 1
        elif movelist[next][1] == 'L':
            if direct == 1:
                direct = 4
            else:
                direct -= 1
        next += 1


    # for j in board:
    #     print(j)
print(move)

