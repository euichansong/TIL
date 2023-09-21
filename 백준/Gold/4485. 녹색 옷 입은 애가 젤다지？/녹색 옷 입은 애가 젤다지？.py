import heapq


def dijkstra(starti, startj):
    pq = []
    heapq.heappush(pq, (matrix[starti][startj], starti, startj))
    distance[starti][startj] = matrix[starti][startj]
    while pq:
        nw, ni, nj = heapq.heappop(pq)
        if distance[ni][nj] < nw:
            continue
        for newi, newj in [[ni+1, nj], [ni, nj+1], [ni-1, nj], [ni, nj-1]]:
            if 0 <= newi < n and 0 <= newj < n:
                new_cost = distance[ni][nj] + matrix[newi][newj]
                if distance[newi][newj] <= new_cost:
                    continue
                distance[newi][newj] = new_cost
                heapq.heappush(pq, (new_cost, newi, newj))

cnt = 1
while True:
    n = int(input())

    if n == 0:
        break
    else:
        matrix = [list(map(int, input().split())) for _ in range(n)]
        distance = [[1e9] * n for _ in range(n)]
        dijkstra(0, 0)
        # print(distance)
        print(f'Problem {cnt}: {distance[n-1][n-1]}')
        cnt += 1