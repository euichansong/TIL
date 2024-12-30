import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int, input().split())
adj = [[] for _ in range(n+1)]


def bfs(s,e):
    q = deque()
    visited = [0] * (n+1)
    q.append(s)
    visited[s] = 1
    ans = 0
    while q:
        t = q.popleft()
        
        if t == e:
            return visited[t]
        for end, wei in adj[t]:
            if visited[end] == 0:
                q.append(end)
                visited[end] =  visited[t] + wei


for _ in range(n-1):
    s,e,w = map(int, input().split())
    adj[s].append([e,w])
    adj[e].append([s,w])

for _ in range(m):
    s,e = map(int, input().split())
    p = bfs(s,e)
    print(p-1)



