"""
1 초	256 MB

2 ≤ N ≤ 30,000, 2 ≤ d ≤ 3,000,


벨트 위에는 같은 종류의 초밥이 둘 이상 있을 수 있다
참가할 경우 추가로 제공
>> 참가하지 않는 경우의 수도 생각해야 할듯

set?
슬라이딩윈도우?

"""

# 접시수, 초밥가짓수, 연속해서먹는 접시수, 쿠폰번호
n,d,k,c = map(int, input().split())
belt = [int(input()) for _ in range(n)]

# k길이만큼 벨트 추가
belt += belt[:k-1]

ans = 0
for i in range(n):
    now = len(set(belt[i:i+k] + [c]))
    ans = max(now,ans)
print(ans)
