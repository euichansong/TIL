"""
nm이 8이니까 브루트포스 가능할듯
0이 갯수가 안전영역
bfs 쓰자
64 c 3 >> 41664 가능할듯?

"""
import sys, copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def bfs(virus, arr):
    q = deque()
    for x, y in virus:
        q.append([x, y])
        while q:
            px, py = q.popleft()
            for vx, vy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx = vx + px
                ny = vy + py
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    q.append([nx, ny])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    return cnt

# 0 좌표, 바이러스 좌표 찾기
zero = []
virus = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            zero.append([i,j])
        if matrix[i][j] == 2:
            virus.append([i,j])
# 벽 세울수 있는 모든 좌표 조합
wallcombi = list(combinations(zero,3))

answer = 0
for i,j,k in wallcombi:
    arr = copy.deepcopy(matrix)
    arr[i[0]][i[1]] = 1
    arr[j[0]][j[1]] = 1
    arr[k[0]][k[1]] = 1
    answer = max(answer,bfs(virus,arr))
print(answer)

