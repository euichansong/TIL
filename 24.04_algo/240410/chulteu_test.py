import sys
from collections import deque

n, m = map(int, input().split())

matrix = [[] for _ in range(n + 1)]
matrix_r = [[] for _ in range(n + 1)]
for i in range(m):
    start, end = map(int, input().split())
    matrix[start].append(end)
    matrix_r[end].append(start)

s, t = map(int, input().split())


def bfs(start, matrix, visited):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        tt = q.popleft()
        for next in matrix[tt]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = 1
    return visited


from_s = [0] * (n + 1)
# s->t 1로 미리 세팅 한번만 갈 수 있게
from_s[t] = 1
bfs(s, matrix, from_s)
print(from_s)

from_t = [0] * (n + 1)
# t->s 1로 미리 세팅 한번만 갈 수 있게
from_t[s] = 1
bfs(t, matrix, from_t)
print(from_t)

to_s = [0] * (n + 1)
bfs(s, matrix_r, to_s)
print(to_s)

to_t = [0] * (n + 1)
bfs(t, matrix_r, to_t)
print(to_t)
answer = 0

for i in range(1, n + 1):
    # 출발,도착점은 무조건 한번만 지나는데, 이렇게 bfs돌리면 모든 곳에서 지난다고 뜸
    # 그래서 출발,도착점은 건너뛰고 계산
    if i == s or i == t:
        continue
    if from_s[i] and from_t[i] and to_s[i] and to_t[i]:
        answer += 1

print(answer)


