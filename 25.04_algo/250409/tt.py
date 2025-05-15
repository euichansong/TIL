## 틀린코드!!!!!!!!!!!!!!!!!!!!!!!!!!!
import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline



def q_check(temp_lst):
    global q

    if temp_lst[0] == temp_lst[1] == temp_lst[2]:
        print(1)
        sys.exit()

    temp_lst.sort()

    if visited[temp_lst[0]][temp_lst[2]] == 0:
        visited[temp_lst[0]][temp_lst[2]] = 1
        q.append(temp_lst)
    return


A, B, C = map(int, input().split())

# 3의 배수인지 확인
if (A + B + C) % 3 != 0:
    print(0)
    sys.exit()

target = (A + B + C) // 3

visited = [[0] * 1501 for _ in range(1501)]
q = deque([[A, B, C]])
visited[min(A, B, C)][max(A, B, C)] = 1

while q:
    num_lst = q.popleft()
    num_lst.sort()

    if num_lst[0] == num_lst[1] == num_lst[2]:
        print(1)
        sys.exit()

    # 1. min, mid 계산
    temp_lst = [num_lst[0] * 2, num_lst[1] - num_lst[0], num_lst[2]]
    q_check(temp_lst)

    # 2. min, max 계산
    temp_lst = [num_lst[0] * 2, num_lst[1], num_lst[2] - num_lst[0]]
    q_check(temp_lst)

    # 3. mid, max 계산
    temp_lst = [num_lst[0], num_lst[1] * 2, num_lst[2] - num_lst[1]]
    q_check(temp_lst)