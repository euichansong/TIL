# -> dfs 실행될때마다 1개씩 남기고 연결된 모든 돌 삭제 가능하기 때문
from typing import List
from collections import deque


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def bfs(i):
            q = deque()
            q.append(i)
            visited[i] = 1
            num_stones = 0
            while q:
                index = q.popleft()
                # 제거 가능한 돌의 갯수
                num_stones += 1
                nx, ny = stones[index]
                for j in range(len(stones)):
                    if visited[j] == 0 and (nx == stones[j][0] or ny == stones[j][1]):
                        q.append(j)
                        visited[j] = 1
            return num_stones

        visited = [0] * len(stones)
        cnt = 0

        for i in range(len(stones)):
            if visited[i] == 0:
                # bfs한번 돌면서 제거 가능한 돌의 갯수
                del_stones = bfs(i)
                # 돌의 갯수에서 1개는 남겨야 최대 갯수
                # 섬이라고 생각하면 된다
                cnt += del_stones - 1

        return cnt
# 메모리 초과
# from collections import deque
# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         def bfs(sx,sy):
#             max_stone = max(map(max,stones))
#             visited = [[0] * (max_stone+1) for _ in range(max_stone+1)]
#             q = deque()
#             q.append([sx,sy])
#             visited[sx][sy] = 1
#             while q:
#                 nx,ny = q.popleft()
#                 for x,y in stones:
#                     if nx == x or ny == y and visited[x][y] == 0:
#                         q.append([x,y])
#                         visited[x][y] = visited[nx][ny] + 1
#             max_s = max(map(max,visited))
#             return max_s
#         answerlist =[]
#         for i,j in stones:
#             aa = bfs(i,j)
#             answerlist.append(aa)
#         return max(answerlist)