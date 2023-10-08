from collections import deque
import sys
input = sys.stdin.readline


def bfs_g1(start):
    global sum_group1
    q = deque()
    q.append(start)
    visited_group1[start] = 1
    while q:
        t = q.popleft()
        sum_group1 += people[t]
        for next_point in adj[t]:
            if visited_group1[next_point] == 0:
                q.append(next_point)
                visited_group1[next_point] = 1


def bfs_g2(start):
    global sum_group2
    q = deque()
    q.append(start)
    visited_group2[start] = 1
    while q:
        t = q.popleft()
        sum_group2 += people[t]
        for next_point in adj[t]:
            if visited_group2[next_point] == 0:
                q.append(next_point)
                visited_group2[next_point] = 1


n = int(input())
adj = [[]]
people = [0] + list(map(int, input().split()))
min = 1e9
for w in range(1, n+1):
    nearlist = list(map(int, input().split()))
    adj.append(nearlist[1:])
# 비트연산으로 부분집합 만들기
for i in range(1, (1 << n) // 2):
    group1 = []
    group2 = []
    for j in range(n):
        if i & (1 << j):
            group1.append(j+1)
        else:
            group2.append(j+1)
    # 그룹별 합 , 방문 리스트 만들기
    sum_group1 = 0
    sum_group2 = 0
    visited_group1 = [0] * (n + 1)
    visited_group2 = [0] * (n + 1)
    # 상대 그룹 방문 안하게 만들기
    for num in group1:
        visited_group2[num] = 1
    for num in group2:
        visited_group1[num] = 1

    start_g1 = group1[0]
    start_g2 = group2[0]
    bfs_g1(start_g1)
    bfs_g2(start_g2)
    flag1 = True
    flag2 = True
    # 연결이 다 되어있는지 확인
    for num in visited_group1[1:]:
        if num == 0:
            flag1 = False
            break
    for num in visited_group2[1:]:
        if num == 0:
            flag2 = False
            break
    # 연결이 잘 되어있으면 최소값 찾기
    if flag1 is True and flag2 is True:
        want_min = abs(sum_group1 - sum_group2)
        if min > want_min:
            min = want_min
# 연결선이 없다면 -1
if min == 1e9:
    print(-1)
else:
    print(min)
