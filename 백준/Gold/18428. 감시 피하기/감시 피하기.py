"""
복도 장애물 학생 안된다
상하좌우 장애물 없으면 무한

3개 장애물
백트네;
t, s, o

2 초	256 MB
"""

"""
이거 브루트포스?
"""
from itertools import combinations
n = int(input())
mat = [list(input().split()) for _ in range(n)]
xlist = []
tlist = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == 'X':
            xlist.append([i,j])
        if mat[i][j] == 'T':
            tlist.append([i,j])

# 4방향 검사
def check(x, y):
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        for p in range(1, n):
            nx = x + dx * p
            ny = y + dy * p
            if not (0 <= nx < n and 0 <= ny < n):
                break
            if mat[nx][ny] == 'O':
                break
            if mat[nx][ny] == 'S':
                return False
    return True

# x좌표 리스트 뽑아서 3개 조합 에 장애물 'O' 대입 
for (i1, j1), (i2, j2), (i3, j3) in combinations(xlist, 3):
    # 장애물 넣기
    mat[i1][j1] = 'O'
    mat[i2][j2] = 'O'
    mat[i3][j3] = 'O'
    flag = True
    for ti, tj in tlist:
        if not check(ti, tj):
            flag = False
            break
    if flag:
        print("YES")
        break
    # 되돌리기
    mat[i1][j1] = 'X'
    mat[i2][j2] = 'X'
    mat[i3][j3] = 'X'

else:
    print("NO")



