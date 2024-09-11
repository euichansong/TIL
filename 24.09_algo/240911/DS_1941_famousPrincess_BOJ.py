import sys

input = sys.stdin.readline
matrix = [list(input()) for _ in range(5)]

answer = 0
selectlist = []
def dfs(len,cnt,sx,sy,select):
    global answer
    if len == 7:
        selected_sorted = sorted(select)
        # 중복되지 않은 좌표 조합이면 추가
        if selected_sorted not in selectlist:
            selectlist.append(selected_sorted)
            if cnt >= 4:
                answer += 1
        return

    for x,y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nx = x + sx
        ny = y + sy
        if 0 <= nx < 5 and 0 <= ny < 5 and [nx,ny] not in select:
            select.append([nx,ny])
            if matrix[nx][ny] == 'S':
                dfs(len+1,cnt+1,nx,ny,select)
            else:
                dfs(len + 1, cnt, nx, ny,select)
            select.pop()

for i in range(5):
    for j in range(5):
        select = [[i,j]]
        if matrix[i][j] == 'S':
            dfs(1,1,i,j,select)
        else:
            dfs(1, 0, i, j,select)
        # print("=================")
print(answer)
