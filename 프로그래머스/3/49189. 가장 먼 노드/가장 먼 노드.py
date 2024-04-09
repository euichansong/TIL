from collections import deque
def solution(n, edge):
    m = len(edge)
    adj = [[] for _ in range(n+1)]
    for i in range(m):
        a = edge[i][0]
        b = edge[i][1]
        adj[a].append(b)
        adj[b].append(a)
    
    def bfs (start):
        visited = [0] * (n+1)
        q = deque()
        q.append(start)
        visited[start] = 1
        while q:
            t = q.popleft()
            for next in adj[t]:
                if visited[next] == 0:
                    q.append(next)
                    visited[next] = visited[t] + 1
        return visited
    answer = 0
    ans = bfs(1)
    max_len = max(ans)
    for i in ans:
        if i == max_len:
            answer += 1
    return answer