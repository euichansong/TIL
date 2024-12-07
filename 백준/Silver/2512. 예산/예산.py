n = int(input())
budget = list(map(int, input().split()))
m = int(input())
budget.sort()
total = sum(budget)
# l = budget[0]
l = 1
r = budget[-1]
if m >= total:
    print(r)
else:
    while l <= r:
        # 총 사용 예산
        money = 0
        # 중간점 - 각 지방의 상한점 역할
        mid = (l+r) // 2
        for i in budget:
            # 각 지방에서 사용할 수 있는 금액이 상한점을 넘어서는 경우
            if i - mid > 0:
                # 상한점만 사용 예산에 더해주고
                money += mid
            # 상한점 안넘으면
            else:
                # 지방의 최대예산을 사용
                money += i
        # 총 사용 예산이 국가 예산 이내면
        if money <= m:
            # 상한액을 늘린다
            l = mid + 1
        else:
            # 아니면 상한액을 줄인다
            r = mid - 1 
    print(r)
