"""
# 소요시간 3일 순 코딩시간 12시간?
가상의 행 생각하는게 힘들었고, bfs dict로 풀려다가 시간초과 발생
dict가 시간복잡도가 O(1)이여도,
for문에서 시간복잡도는 dict의 길이기 때문에 dict가 아무의미없었다.
"""
"""
문제 정리
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
sys.stdin = open('3input.txt')

r, c, k = map(int, input().split())
# 가상의 행 생성
r = r + 2
forest = [[0] * c for _ in range(r)]
ans = 0
golem_cnt = 0
# 숲 초기화
def reset():
    global forest
    global r
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
# sr ci가 골렘 정령 좌표
def golem(sr,ci,di,r,c):
    global forest
    global golem_cnt
    flag = True
    # 가상의 행에 정령 있는경우 리셋
    if 0 <= sr <= 1:
        flag = False
        return flag

    for x,y in [[0,0],[0,1],[1,0],[-1,0],[0,-1]]:
        if not(0<= sr+x < r and 0<= ci + y < c):
            flag = False
            return flag
        else:
            if 0 <= sr+x <= 1:
                flag = False
                return flag
            else:
                forest[sr+x][ci+y] = golem_cnt
    if di == 0:
        forest[sr -1][ci] = -golem_cnt
    elif di == 1:
        forest[sr][ci+1] = -golem_cnt
    elif di == 2:
        forest[sr+1][ci] = -golem_cnt
    else:
        forest[sr][ci-1] = -golem_cnt
    return flag

def bfs(sx, sy, r, c):
    q = deque()
    q.append((sx, sy))
    visited = [[0] * c for _ in range(r)]
    visited[sx][sy] = 1
    max_r = sx

    while q:
        px, py = q.popleft()
        max_r = max(max_r, px)

        # 현재 위치가 출구인 경우
        if forest[px][py] < 0:
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nx, ny = px + dx, py + dy

                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                    # 다른 출구로 이동
                    if forest[nx][ny] < 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                    # 연결된 골렘으로 이동
                    elif forest[nx][ny] > 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny))

        # 현재 위치가 몸체(+값)인 경우
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = px + dx, py + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if forest[nx][ny] != 0 and abs(forest[px][py]) == abs(forest[nx][ny]):
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    return max_r - 1

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
    golem_cnt += 1
    # 숲에 골렘 넣기
    if not golem(sr, ci, di,r,c):
        reset()
    else:
        # #골렘 내리기
        max_r_bfs = bfs(sr,ci,r,c)
        ans += max_r_bfs
    #     print(max_r_bfs)
    # for i in range(2,r):
    #     print(forest[i])
    # print("=====================")
print(ans)
"""dict 사용 시간초과 코드
import sys
from collections import deque
sys.stdin = open('11501.txt')

r, c, k = map(int, input().split())
# 가상의 행 생성
r = r + 2
forest = [[0] * c for _ in range(r)]
dict = {}
ans = 0
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
            aa = sr + nr
            bb = sc + nc
            if sr+nr < r and 0<= sc+nc < c and forest[sr+nr][sc+nc] == 0:

                cc = forest[aa][bb]
                continue
            else:
                tf = False
                break
    return tf
"""

"""
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
                aa = sr + nr
                bb = sc + nc
                cc = forest[aa][bb]
                continue
            else:
                tf = False
                break
    return tf

# 0,1,2,3은 북, 동, 남, 서
# sr ci가 골렘 정령 좌표
def golem(sr,ci,di,r,c):
    global forest
    flag = True
    val = []
    # 가상의 행에 정령 있는경우 리셋
    if 0 <= sr <= 1:
        flag = False
        return flag

    for x,y in [[0,0],[0,1],[1,0],[-1,0],[0,-1]]:
        if not(0<= sr+x < r and 0<= ci + y < c):
            flag = False
            return flag
        else:
            if 0 <= sr+x <= 1:
                flag = False
                return flag
            forest[sr+x][ci+y] = 1
            val.append([sr+x,ci+y])
    if di == 0:
        forest[sr -1][ci] = 4
    elif di == 1:
        forest[sr][ci+1] = 4
    elif di == 2:
        forest[sr+1][ci] = 4
    else:
        forest[sr][ci-1] = 4
    key = (sr,ci)
    if key not in dict:
        dict[key] = val
    return flag

def bfs(sx,sy,r,c):
    q = deque()
    q.append([sx,sy])
    visited = [[0] * c for _ in range(r)]
    visited[sx][sy] = 1
    max_r = 0
    while q:
        px,py = q.popleft()
        max_r = max(px,max_r)
        if max_r-1 == r:
            return max_r-1
        # 정령이 dict의 key, 골렘의 몸체가 value
        for nx,ny in dict[(px,py)]:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                max_r = max(nx, max_r)
                if max_r - 1 == r:
                    return max_r - 1
                # 출구인 경우 4방향 탐색해 넘어갈수 있는 골렘 있는지 확인
                if forest[nx][ny] == 4:
                    for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        dmx = nx+dx
                        dmy = ny+dy
                        if 0 <= dmx < r and 0 <= dmy < c and visited[dmx][dmy] == 0:
                            # 이 좌표가 value에 들어있으면
                            for k,v in dict.items():
                                if [dmx,dmy] in v:
                                    # k는 dict의 중심점 이니까 그걸 q에 넣어준다
                                    # q에 골렘의 중심점만 들어간다
                                    visited[k[0]][k[1]] = 1
                                    q.append(k)
    return max_r-1
"""
"""
그러면 처음도 4방향을 도는게 아니라 dict에서 찾아서 그 좌표를 q에 넣고 visited를 해줘 
> 4인경우 옆골렘까지 q에 넣어야해 4의 옆 좌표가 존재 한다면
> 그 좌표가 들어있는 골렘의 중심을 dict에서 찾아서 q에 중심점을 넣어
> dict를 중심점을 key로 하는게 맞지
"""

"""
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
        continue

    #골렘 내리기
    if dict:
        max_r_bfs = bfs(sr,ci,r,c)
        # print(max_r_bfs)
        ans += max_r_bfs

    # for i in range(r):
    #     print(forest[i])
    # print("=====================")
print(ans)
"""