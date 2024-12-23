"""
역들의 고유번호는 서로 다르다
다음역은 시계방향 인접한 역
이전역은 반시계방향

공사 m번 시행

BN 다음역 출력 그 사이에 j번인 역 설립
BP 이전역 출력 그 사이에 j번인 역 설립
CN 다음역 폐쇄 그 역의 고유번호 출력
CP 이전역 폐쇄 그 역의 고유번호 출력
"""

from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
# 역의 고유 변호
station = list(map(int, input().split()))
back = [0] * 1000001
front = [0] * 1000001
for i in range(n):
    # 이전값 저장
    back[station[i]] = station[i-1]
    # 다음값 저장
    front[station[i-1]] = station[i]
for _ in range(m):
    order = list(input().split())
    if order[0] == 'BN':
        i = int(order[1])
        j = int(order[2])
        # 다음역 출력
        nextS = front[i]
        print(nextS)
        # i j nextS 순
        front[i] = j
        front[j] = nextS
        back[j] = i
        back[nextS] = j
    elif order[0] == 'BP':
        i = int(order[1])
        j = int(order[2])
        backS = back[i]
        print(backS)
        # backS j i 순 
        front[j] = i
        front[backS] = j
        back[i] = j
        back[j] = backS
    # 다음역 폐쇄 그 역 고유번호
    elif order[0] == 'CN':
        # i front[i] front[front[i]] 순서
        i = int(order[1])
        nextS = front[i]
        print(nextS)
        # 다음다음역
        nextnextS = front[nextS]
        front[i] = nextnextS
        back[nextnextS] = i
    # 이전역 폐쇄 그 역 고유번호
    else:
        i = int(order[1])
        backS = back[i]
        print(backS)
        # back[back[i]] back[i] i 순서
        # 이전 이전역
        backbackS = back[backS]
        front[backbackS] = i
        back[i] = backbackS
