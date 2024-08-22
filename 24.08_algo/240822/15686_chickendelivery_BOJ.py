"""
좌표를 뽑아서 조합을 만들고 각각 집에서 거리 계산
"""
import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

# 치킨집, 집 좌표 구하기
clist = []
hlist = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            clist.append([i,j])
        elif city[i][j] == 1:
            hlist.append([i,j])
# 치킨집 가능 조합 만들기
combination = list(combinations(clist,m))
min_ccd = 1e9
# 짤 수 있는 모든 치킨집 조합
for combi in combination:
    # 집과 치킨집 거리 총 계산
    ccd = 0
    # 전체 집 조합
    for h in hlist:
        # 현재 집에서 가장 가까운 치킨집 거리 계산
        min_hmd = 1e9
        for c in combi:
            distance = abs(h[0] - c[0]) + abs(h[1] - c[1])
            min_hmd = min(distance,min_hmd)
        ccd += min_hmd
    min_ccd = min(ccd,min_ccd)
print(min_ccd)