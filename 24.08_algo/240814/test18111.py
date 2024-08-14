import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]
maxh = max(map(max,land))
minh = min(map(min,land))
min_time = 1e9
height = 0
for layer in range(minh,maxh+1):
    add = 0
    remove = 0

    for i in range(N):
        for j in range(M):

            if land[i][j] <= layer:
                add += layer - land[i][j]
            else:
                remove += land[i][j] - layer

    if add > remove + B:
        continue

    if add + (remove * 2) <= min_time:
        min_time = add + (remove * 2)
        height = layer

print(min_time, height)