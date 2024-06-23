from collections import deque
import sys
input = sys.stdin.readline


n, m, r = map(int, input().split())
adj =[[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


def BFS(start):
    global order
    global cnt
    visited = [-1] * (n+1)
    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        now = q.popleft()
        order[now] = cnt
        cnt += 1
        adj[now].sort()
        for next in adj[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + 1
                q.append(next)
    return visited

cnt = 1
order = [0] * (n+1)
vi = BFS(r)
# print(order)
# print(vi)
res = 0
for i in range(1, len(order)):
    res += (order[i] * vi[i])
print(res)