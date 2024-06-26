from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
abilities = list(map(int, input().split()))
abilities.sort()

abilities = deque(abilities)
team_count = 0

while len(abilities) > 1:
    if abilities[0] + abilities[-1] >= m:
        # 가장 작은 값과 가장 큰 값을 합쳐서 조건을 만족하면
        abilities.popleft()  # 가장 작은 값을 제거
        abilities.pop()      # 가장 큰 값을 제거
        team_count += 1
    else:
        # 조건을 만족하지 않으면 가장 작은 값만 제거
        abilities.popleft()

print(team_count)