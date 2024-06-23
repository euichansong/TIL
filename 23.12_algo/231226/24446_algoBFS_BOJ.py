from collections import deque
import sys
input = sys.stdin.readline


n, m, r = map(int, input().split())
adj = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
# print(adj)


def BFS(start):
    visited = [-1] * (n+1)
    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        t = q.popleft()
        for w in adj[t]:
            if visited[w] == -1:
                q.append(w)
                visited[w] = visited[t] + 1

    return visited

a = BFS(r)
for i in range(1,len(a)):
    print(a[i])
