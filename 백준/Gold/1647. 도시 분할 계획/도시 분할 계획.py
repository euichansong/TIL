import heapq
import sys
input = sys.stdin.readline

def prim(start):
    pq = []
    visited = [0] * (n+1)
    heapq.heappush(pq, (0, start))
    result = []
    while pq:
        weight, node = heapq.heappop(pq)
        if visited[node] == 1:
            continue
        visited[node] = 1
        result.append(weight)
        if len(result) == n:
            break
        for next_node, new_w in graph[node]:

            if new_w == 0 or visited[next_node] == 1:
                continue
            heapq.heappush(pq, (new_w, next_node))
    return sum(result) - max(result)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, w = map(int, input().split())
    graph[a].append([b,w])
    graph[b].append([a,w])
print(prim(1))