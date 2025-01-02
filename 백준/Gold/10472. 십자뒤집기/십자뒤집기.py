from itertools import product
import copy,sys
input = sys.stdin.readline

t = int(input())

def click(mat,x,y):
    dx = [0,1,0,-1,0]
    dy = [0,0,1,0,-1]
    for i in range(5):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < 3 and 0 <= ny < 3:
            if mat[nx][ny] == '*':
                mat[nx][ny] = '.'
            else:
                mat[nx][ny] = '*'

def pro(board):
    global min_clicks
    mat = list(product((0,1), repeat=9))
    for i in mat:
        basic = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        for j in range(9):
            if i[j] == 1:
                nx = j // 3
                ny = j % 3
                # print(mat,nx,ny)
                click(basic,nx,ny)

        if basic == board:
            min_clicks = min(sum(i),min_clicks)


for _ in range(t):
    board = [list(input().strip()) for _ in range(3)]
    basic = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    min_clicks = float('inf')
    pro(board)
    print(min_clicks)