"""
다익스트라
근데 다익스트라는 최소값을 반환하는데
문제에선 최대값 찾는다
"""
import heapq
from typing import List
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        # 간선 만들기
        graph = [[] for _ in range(n)]
        for i in range(len(succProb)):
            s = edges[i][0]
            e = edges[i][1]
            w = succProb[i]
            # 방향이 없다
            graph[s].append([e,w])
            graph[e].append([s,w])

        # 다익스트라
        q = []
        probability = [0] * n
        # 가중치가 앞으로
        heapq.heappush(q,[-1,start_node])
        probability[start_node] = 1
        while q:
            ga,node = heapq.heappop(q)
            # -를 붙이면 최소값을 찾는게 아니라 최대값을 찾을듯?
            ga = -ga
            # 노드가 end면 나간다
            if node == end_node:
                return ga
            # 다음 노드와 가중치
            for next_node, next_waight in graph[node]:
                # 새로운 가중치는 원래 가중치와 다음 노드의 가중치를 곱한것
                new_waight = ga*next_waight
                # 만약 원래 확률보다 작으면 넘어간다
                # 작거나 같아야 메모리 초과 안한다;;
                if new_waight <= probability[next_node]:
                    continue
                # -로 넣어야 최대치가 나온다
                heapq.heappush(q,[-new_waight,next_node])
                probability[next_node] = new_waight
        return 0
# n edges succProb start_node end_node


def main():
    # 인풋값
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    start_node = 0
    end_node = 2
    # n = 3
    # edges = [[0, 1], [1, 2], [0, 2]]
    # succProb = [0.5, 0.5, 0.3]
    # start_node = 0
    # end_node = 2

    sol = Solution()
    result = sol.maxProbability(n, edges, succProb, start_node, end_node)
    print(result)


if __name__ == "__main__":
    main()