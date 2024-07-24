n = int(input())
moving = list(input())

idx = [[0,0]]

# 남,동,북,서
dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 남쪽보는데 R이면 서 , L이면 동
nx = 0
ny = 0

direction = 0
for i in range(n):
    if moving[i] == 'F':
        nx += dx[direction]
        ny += dy[direction]
        idx.append([nx, ny])
    elif moving[i] == 'R':
        direction = (direction + 3) % 4

    elif moving[i] == 'L':
        direction = (direction + 1) % 4

xmin = min(idx, key= lambda x:x[0])[0]
xmax = max(idx, key= lambda x:x[0])[0]
ymin = min(idx, key= lambda x:x[1])[1]
ymax = max(idx, key= lambda x:x[1])[1]

xlen = abs(xmax-xmin)+1
ylen = abs(ymax-ymin)+1

map = [['#'] * ylen for _ in range(xlen)]

for i in range(len(idx)):
    idx[i][0] -= xmin
    idx[i][1] -= ymin
    map[idx[i][0]][idx[i][1]] = '.'
for row in map:
    print(''.join(row))