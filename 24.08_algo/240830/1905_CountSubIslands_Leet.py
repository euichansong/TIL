"""
global answer로 시도하려니까 안되는데;

정사각형이 아니라 ny의 범위를 바꿔줘야 한다
"""
from collections import deque
from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        answer = 0

        def bfs(startx, starty):
            q = deque()
            flag = True
            q.append([startx, starty])
            while q:
                px, py = q.popleft()
                if grid1[px][py] == 0:
                    flag = False

                for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nx = px + x
                    ny = py + y
                    if 0 <= nx < len(grid2) and 0 <= ny < len(grid2[0]) and grid2[nx][ny] == 1:
                        q.append([nx, ny])
                        grid2[nx][ny] = 0
            return flag

        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1:
                    if bfs(i, j):
                        answer += 1
        return answer