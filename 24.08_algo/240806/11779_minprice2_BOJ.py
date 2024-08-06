import heapq, sys
input = sys.stdin.readline
n = int(input())
m = int(input())
seplist = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,p = map(int, input().split())
    seplist[s].append([e,p])
start, end = map(int, input().split())
distance = [1e9] * (n+1)
# 방문 도시 저장
citylist = [-1] * (n+1)
def dijkstra(start):
    hq = []
    heapq.heappush(hq,(0,start))
    distance[start] = 0
    while hq:
        dist, next = heapq.heappop(hq)
        if distance[next] < dist:
            continue
        citylist.append(next)
        for city,cost in seplist[next]:
            newcost = dist+cost
            if distance[city] <= newcost:
                continue
            distance[city] = newcost
            # 방문 도시 전부 저장
            citylist[city] = next
            heapq.heappush(hq,(newcost,city))

dijkstra(start)
print(distance[end])

# 가장 최근에 방문한 도시를 역추적하면 최단 경로가 나온다
# citylist[5] = 4
# citylist[4] = 1
# citylist[1] = -1
answer = []
nc = end

while nc != -1:
    answer.append(nc)
    nc = citylist[nc]

print(len(answer))
answer.reverse()
print(*answer)