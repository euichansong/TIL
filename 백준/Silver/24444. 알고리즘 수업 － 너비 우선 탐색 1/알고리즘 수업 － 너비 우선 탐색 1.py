from collections import deque
import sys
input = sys.stdin.readline


def BFS(start):
    global cnt
    q = deque()
    visited = [0] * (n+1)
    visited[start] = cnt
    q.append(start)
    while q:
        t = q.popleft()
        # 오름차순 정렬
        adj[t].sort()
        for w in adj[t]:
            if visited[w] == 0:
                q.append(w)
                # 순서
                cnt += 1
                visited[w] = cnt

    return visited


n, m, start = map(int, input().split())
adj = [[] for _ in range(n+1)]
# 순서 위해서
cnt = 1
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visit = BFS(start)
# print(visit[1:])
for i in visit[1:]:
    print(i)

