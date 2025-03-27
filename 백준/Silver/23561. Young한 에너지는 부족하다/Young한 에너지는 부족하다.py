"""
중요한건 중간값 이 에너지라는거

최대 최소 하나씩 빼고 마지막에 남은값 최대값 최소값 뺀게 답일듯?

21 26
22 25

23 24
"""

import sys
input = sys.stdin.readline
n = int(input())
crew = list(map(int, input().split()))
crew.sort()
slice_crew = crew[n:2*n]
answer = max(slice_crew) - min(slice_crew)
print(answer)
