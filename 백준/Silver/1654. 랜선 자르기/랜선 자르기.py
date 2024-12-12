import sys
input = sys.stdin.readline
k,n = map(int, input().split())
rlist = [int(input()) for _ in range(k)]
l = 1
r = max(rlist)
ans = 0
while l <= r:
    mid = (l + r) // 2

    # 자른 갯수
    cut = 0
    for ran in rlist:
        cut += (ran // mid)
    # 자른 갯수가 주어진거보다 많거나 적으면 중앙 재 정렬
    if cut >= n:
        
        l = mid + 1
        ans = mid
        
    else:
        r = mid - 1


print(ans)