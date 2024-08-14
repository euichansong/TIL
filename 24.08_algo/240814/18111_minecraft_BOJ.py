"""
평균 계산하고 그걸로?
땅 높이 256 초과 안된다 음수 안된다
-는 2초
더하는건 1초 답이 여러개면 땅의 높이가 가장 높은것으로

평균으로 하면 틀린다 갯수 없는 경우 있어서

최소값 기준으로
"""

n,m,b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
maxh = max(map(max,land))
minh = min(map(min,land))
answer = []
for t in range(minh,maxh+1):
    for i in range(n):
        for j in range(m):
            pass

