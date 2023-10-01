from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    q = deque()
    visited[start] = 1
    q.append(start)
    while q:
        t = q.popleft()
        for w in adj[t]:
            # 방문한적 없으면
            if visited[w] == 0:
                # 방문하고 그 값이 부모노드
                visited[w] = t
                q.append(w)


n = int(input())
adj = [[] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

bfs(1)
for i in range(2,n+1):
    print(visited[i])