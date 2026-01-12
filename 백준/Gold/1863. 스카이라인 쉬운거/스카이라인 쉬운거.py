"""
2 초	128 MB

힌트 기준 세로줄에서 가장 높은거 

고도가 바뀌는 지점의 좌표 x와 y q에 넣고 빼기?

0이 나오면 컷
처음꺼 큐에 추가 
y좌표가 이전거 보다 크면 추가 작으면 패스 ?? 그럼 마지막꺼 1을 어떻게 추가? 마지막 q에 남아있으면 무조건 추가?

높이에 따른 
비교군 시작 크면 비교군 변경 작으면 건물 추가 0이면 리셋 마지막이면 추가

이 예시 뚫으면 될듯
6
1 2
3 3
6 2
8 1
9 3
10 1

"""
from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
point = deque([list(map(int, input().split())) for _ in range(n)])
s = []
ans = 0
while point:
    px, py = point.popleft()
    # 0이면 리셋, 건물 추가
    if py == 0:
        ans += len(s)
        s = []
    else:
        # 비교군 보다 작으면 건물 추가
        while s and s[-1] > py:
            ans += 1
            s.pop()
        # 비교군 없거나 비교군 보다 크면 비교군 추가
        if not s or s[-1] < py:
            s.append(py)

ans += len(s)
print(ans)
