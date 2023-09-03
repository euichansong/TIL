# 속도 빠르게
import sys
# 재귀 깊이 증가
sys.setrecursionlimit(10**9)
n, m, r = map(int, sys.stdin.readline().split())
# 방문
visited = [0] * (n+1)
adj_m = [[] for _ in range(n+1)]
cnt = 1
# 간선
for i in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    adj_m[v1].append(v2)
    adj_m[v2].append(v1)
# 함수
def dfs(r,visited, adj_m):
    # 카운트 증가
    global cnt
    # 방문하면 카운트
    visited[r] = cnt
    # 오름차순
    adj_m[r].sort()
    for w in adj_m[r]:
        # 방문하지 않았으면
        if visited[w] == 0:
            cnt += 1
            # 카운트
            visited[w] = cnt
            # 재귀
            dfs(w, visited, adj_m)
# 함수 시작
dfs(r, visited, adj_m)
# i번째 줄 정점 방문 순서
for i in range(1, n+1):
    print(visited[i])