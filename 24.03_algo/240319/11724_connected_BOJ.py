from collections import deque
import sys
input = sys.stdin.readline
def BFS(start):
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        t = q.popleft()
        for next in adj[t]:
            if visited[next] == 0:
                visited[next] = visited[t] + 1
                q.append(next)
    return visited


n, m = map(int,input().split())
adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0
# 방향이 없다 >> 양방향 간선
for i in range(m):
    start, end = map(int,input().split())
    adj[start].append(end)
    adj[end].append(start)

for i in range(1,n+1):
    if visited[i] == 0:
        BFS(i)
        count += 1
print(count)