"""

heapq는 처음꺼 기준으로 정렬한다
"""
import sys, heapq
input = sys.stdin.readline

n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,t = map(int, input().split())
    graph[s].append([e,t])

def djk(start):
    distance = [1e9] * (n+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            next_town = next[0]
            cost = next[1]

            new_cost = dist + cost
            if distance[next_town] <= new_cost:
                continue
            distance[next_town] = new_cost
            heapq.heappush(q, (new_cost,next_town))
    return distance
"""
t 마을까지 가고 다시 원래대로 돌아가야 한다
원래 마을에서 t까지 최소 + t에서 원래 마을로 
"""
xtn = djk(x)
relist = []
for i in range(1, n+1):
    ntx = djk(i)
    maxt = xtn[i]+ntx[x]
    relist.append(maxt)
print(max(relist))