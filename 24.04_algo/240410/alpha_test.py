import sys

input = sys.stdin.readline


def DFS(ci, cj, visited_lst, N, M, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        ni, nj = ci + di, cj + dj

        if 0 <= ni < N and 0 <= nj < M:
            if visited_lst[ord(map[ni][nj]) - ord('A')] == 0:
                visited_lst[ord(map[ni][nj]) - ord('A')] = 1
                DFS(ni, nj, visited_lst, N, M, cnt + 1)
                visited_lst[ord(map[ni][nj]) - ord('A')] = 0


# dx, dy로 구현하면 시간초과나지 않지만,
# for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]] 로 구현하면 시간초과 발생... 왜지?
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

map = [input().rstrip() for _ in range(N)]

# list로 구현 시 시간초과
# list의 append, pop은 set의 add, remove
# set으로 구현 역시 시간초과
# ord 사용하여 toggle 형식으로 구현
visited_lst = [0] * 26
visited_lst[ord(map[0][0]) - ord('A')] = 1

max_cnt = 0
DFS(0, 0, visited_lst, N, M, 1)

print(max_cnt)