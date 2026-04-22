"""
2 초	128 MB


10억이면 이분탐색인데

한집에 공유기 하나 

1. 최소점 최대점 구해서 c로 나누고 거기서 부터 시작? > 아닌듯?
2. 집 정렬해서 최소점 최대점에 하나씩 놓고 좌표중에 고르면 될듯 > 이건데?
>> 1만 놓으면 되는거 아닌가?
>> 이게 왜 되는거지? l,r이 좌표값이 아닌데
> 짜피 진짜 위치를 구하는게 아니라 거리차이를 구하는거니까 상관없겠지
"""
import sys
input = sys.stdin.readline
n,c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()


# 거리를 구하는거니까 최대거리 
l = 1
r = house[n-1] - house[0]
ans = 0

while l <= r:
    mid = (l + r) // 2
    now = house[0]
    cnt = 1
    for i in range(1,n):
        # 실제 공유기 사이 거리
        dis = house[i] - now
        # 거리가 임의의 중간값보다 크면 설치
        if dis >=  mid:
            # 설치한 공유기 위치 최신화
            now = house[i]
            cnt += 1
            
    # 설치를 더 했다는것은 거리 늘리기 가능하니까 여기서 최대거리 찾기
    if cnt >= c:
        # 중앙값 늘리기 
        l = mid + 1
        ans = max(ans, mid)
    else:
        r  = mid -1

print(ans)



