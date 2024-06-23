import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    start, end, price = map(int, input().split())
    graph[start].append([end,price])

distance = [0] + [1e9] * n
# print(graph)
def dijstra(start):
    # 힙큐
    q = []
    # 힙큐에 값 넣기 (시작점, 가중치 )
    heapq.heappush(q, (start,0))
    distance[start] = 0

    while q:
        # 현재점, 가중치
        now, dist = heapq.heappop(q)
        # 저장된 가중치가 이번 가중치보다 많으면 패스
        if distance[now] < dist:
            continue
        # 현재 점으로 갈 수 있는 (점 + 가중치)
        for next in graph[now]:
            # print(next)
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost
            # 다음점의 가중치보다 새로운 가중치가 크면 패스
            if distance[next_node] <= new_cost:
                continue
            # 아니면 가중치 저장
            distance[next_node] = new_cost
            # 다시 힙큐에 넣기
            heapq.heappush(q, (next_node, new_cost))
# 시작점, 끝점
start_point, end_point = map(int, input().split())

dijstra(start_point)

print(distance[end_point])