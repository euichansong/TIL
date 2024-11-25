"""
우선순위
1. 남쪽 1칸 - 밑에 아무것도 없을때 이동
2. 서쪽으로 회전 - 옆에 이동 가능할때, 출구 방향 변경
3. 동쪽으로 회전 - 옆에 이동 가능할때, 출구 방향 변경
0,1,2,3은 북, 동, 남, 서
4. 최대 이동시 숲 벗어나면 숲 초기화

이동할수 없으면 골렘 이동 가능, 골렘 출구로 나가야 한다
"""
import sys
from collections import deque
sys.stdin = open('input.txt')

r, c, k = map(int, input().split())
forest = [[0] * c for _ in range(r)]
dict = {}

# 숲 초기화
def reset():
    global forest
    global dict
    dict = {}
    forest = [[0] * c for _ in range(r)]

# down
def down(sr,sc,r,c):
    global forest
    tf = True
    for nr,nc in [[2,0],[1,-1],[1,1]]:
        if sr+nr < r and 0<= sc+nc < c and forest[sr+nr][sc+nc] == 0:
            continue
        else:
            tf = False
            break
    return tf

# left
def left(sr,sc,r,c):
    global forest
    tf = True
    for nr,nc in [[0,-2],[-1,-1],[1,-1],[1,-2],[2,-1]]:
        # 보드 밖에 있는지
        if sr + nr < 0:
            continue
        else:
            # 보드 안에 있는지
            if sr+nr < r and 0<= sc+nc < c and forest[sr+nr][sc+nc] == 0:
                continue
            else:
                tf = False
                break
    return tf

# right
def right(sr,sc,r,c):
    global forest
    tf = True
    for nr,nc in [[0,2],[-1,1],[1,1],[1,2],[2,1]]:
        # 보드 밖에 있는지
        if sr + nr < 0:
            continue
        else:
            # 보드 안에 있는지
            if sr+nr < r and 0<= sc+nc < c and forest[sr+nr][sc+nc] == 0:
                continue
            else:
                tf = False
                break
    return tf

# 0,1,2,3은 북, 동, 남, 서
def golem(sr,ci,di,r,c):
    global forest
    flag = True

    val = []
    for x,y in [[0,0],[0,1],[1,0],[-1,0],[0,-1]]:
        if not(0<= sr+x < r and 0<= ci + y < c):
            flag = False
            return flag
        else:
            forest[sr+x][ci+y] = 1
            val.append([sr+x,ci+y])
    if di == 0:
        forest[sr -1][ci] = 4
        key = (sr - 1, ci)

    elif di == 1:
        forest[sr][ci+1] = 4
        key = (sr, ci+1)
    elif di == 2:
        forest[sr+1][ci] = 4
        key = (sr + 1, ci)
    else:
        forest[sr][ci-1] = 4
        key = (sr, ci-1)
    if key not in dict:
        dict[key] = val
    return flag

def bfs(sx,sy,r,c):
    q = deque()
    q.append([sx,sy])
    visited = [[0] * c for _ in range(r)]
    visited[sx][sy] = 1
    max_r = []
    while q:
        px,py = q.popleft()
        for mx,my in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx = mx + px
            ny = my + py
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0:
                if forest[nx][ny] == 1:
                    visited[nx][ny] = visited[px][py] + 1
                    max_r.append(nx)
                elif forest[nx][ny] == 4:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[px][py] + 1
                    max_r.append(nx)
    if max_r:
        print(max(max_r)+1)


# 행 r, 열 c
for start in range(k):
    # 출발열, 출구방향
    ci, di = map(int, input().split())
    # 인덱스 맞춤
    ci -= 1
    # 출발 행
    sr = 0
    while True:
        # 내려가는경우
        if down(sr,ci,r,c):
            sr += 1
        elif sr >= r-2:
            break
        # 왼쪽
        elif left(sr,ci,r,c):
            ci -= 1
            sr += 1
            di = (di + 3) % 4
        # 오른쪽
        elif right(sr,ci,r,c):
            ci += 1
            sr += 1
            di = (di + 1) % 4
        else:
            break

    # 숲에 골렘 넣기
    if not golem(sr, ci, di,r,c):
        reset()

    #골렘 내리기
    # bfs(sr,ci,r,c)
    print(dict)

    for i in range(r):
        print(forest[i])
    print("=====================")
