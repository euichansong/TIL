"""
dp 그래프
1 초	256 MB

00에서 44까지
"""
from collections import deque

n = int(input())
mat = [input().split() for _ in range(n)]

visit = [[0]*n for _ in range(n)]
answer = []

# 좌표, 계산값, 연산자
def dfs(px, py, pz, po):
    if px == n-1 and py == n-1:
        answer.append(pz)
        return

    for dx, dy in [(0,1),(1,0)]:
        nx = px+dx
        ny = py+dy
        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
            cell = mat[nx][ny]
            visit[nx][ny] = 1

            # 연산자인 경우
            if cell in '+-*':
                dfs(nx, ny, pz, cell)
            else:
                # 변환 안하면 안되네
                num = int(cell)
                if po == 'c':
                    calcu = pz
                elif po == '+':
                    calcu = pz + num
                elif po == '-':
                    calcu = pz - num
                else:
                    calcu = pz * num
                dfs(nx, ny, calcu, 'c')
            visit[nx][ny] = 0

visit[0][0] = 1
dfs(0,0,int(mat[0][0]),'c')
print(max(answer), min(answer))

    