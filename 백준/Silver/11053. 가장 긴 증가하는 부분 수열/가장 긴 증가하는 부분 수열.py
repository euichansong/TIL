"""
11
100 1 2 3 101 4 5 6 102 7 8
정답 8
"""
n = int(input())
alist = list(map(int, input().split()))

dp = [1] * n

for i in range(1,n):
    for j in range(i):
        if alist[i] > alist[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
# """
# 11
# 100 1 2 3 101 4 5 6 102 7 8
# 정답 8
# """
# n = int(input())
# alist = list(map(int,input().split()))
#
# dp = [0] * n
# for i in range(n):
#     longlist = []
#     for j in range(i,n):
#         if len(longlist) == 0:
#             longlist.append(alist[j])
#
#         if len(longlist) >= 1:
#             if longlist[-1] < alist[j]:
#                 longlist.append(alist[j])
#     dp[i] = len(longlist)
#     print(longlist)
# print(max(dp))