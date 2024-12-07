"""
가로등 기준 양옆이 최소
"""
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
ga = list(map(int, input().split()))
ga_max = 0
# 가로등 1개일때
if m == 1:
    ga_max = max(ga[0], n - ga[0])
else:
    for i in range(m):
        # 0일때 최소거리
        if i == 0:
            dis = ga[0]
        # 끝점일때 최소거리
        elif i == m - 1:
            dis = n - ga[m-1]
        else:
            # 가로등 사이 최소거리
            dis = (ga[i] - ga[i-1] + 1) // 2
        ga_max = max(ga_max, dis)
print(ga_max)
