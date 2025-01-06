"""
최대 1000 m 
시작하면서 -1하고 시작
편의점 도착 맥스 1000

"""
import sys
input = sys.stdin.readline
from collections import deque
t = int(input())

def bfs(hx,hy,co,fx,fy):
    q = deque()
    visited = [0] * n
    q.append([hx,hy])
    while q:
        tx,ty = q.popleft()
        if abs(fx-tx)+abs(fy-ty) <= 1000:
            print("happy")
            return

        for i in range(len(co)):
            if visited[i] == 0:
                nx,ny = co[i][0],co[i][1]
                distan = abs(tx-nx)+abs(ty-ny)
                if distan <= 1000:
                    visited[i] = 1
                    q.append([nx,ny])

    print("sad")
    return 


# # 현재 점에서 가까운 편의점 순
# def near_combi(nowx, nowy, co):
#     dis = []
#     for cx, cy in co:
#         dist = abs(nowx - cx) + abs(nowy - cy)
#         dis.append([dist, [cx, cy]])
#     dis.sort(key=lambda x: x[0])
#     res = []
#     for _, c in dis:
#         result.append(c)
#     return res

        
for _ in range(t):
    # 편의점 갯수
    n = int(input())
    hx, hy = map(int,input().split())
    co = [list(map(int,input().split())) for i in range(n)]
    fx,fy = map(int,input().split())
    bfs(hx,hy,co,fx,fy)


