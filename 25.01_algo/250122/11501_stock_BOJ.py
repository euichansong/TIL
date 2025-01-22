"""
하나를 산다
원하는만큼 판다
안한다

1
5
1 1 3 1 10
5 초	256 MB
"""
from collections import deque
import sys,copy
sys.stdin = open("11501.txt")
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    sell = 0
    ans = 0
    for i in range(n-1,-1,-1):
        if price[i] < sell:
            ans += sell-price[i]
        else:
            sell = price[i]
    print(ans)


# 5 10 1 2 >> 반례
# for _ in range(t):
#     n = int(input())
#     price = list(map(int, input().split()))
#     sort_p = copy.deepcopy(price)
#     sort_p.sort(reverse=True)
#     buy = deque()
#     idx = 0
#     ans = 0
#     for i in range(n):
#         if price[i]< sort_p[idx]:
#             buy.append(price[i])
#         else:
#             sell = sort_p[idx]
#             if buy:
#                 while buy:
#                     t = buy.popleft()
#                     ans += (sell-t)
#             idx += 1
#     print(ans)




