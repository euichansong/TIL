"""
1 초	512 MB
"""
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visit = list(map(int, input().split()))

now = sum(visit[:x])
max_vi = now  
ans = 1 
for i in range(x, n):
    # 첫 번째 값 제거
    now -= visit[i - x]  
    # 새로운 값 추가
    now += visit[i]  
    if now > max_vi:
        max_vi = now
        ans = 1  
    elif now == max_vi:
        ans += 1  

if max_vi == 0:
    print("SAD")
else:
    print(max_vi)
    print(ans)

# 시간초과
# import sys
# input = sys.stdin.readline
# n,x= map(int, input().split())
# visit = list(map(int, input().split()))
# dp = [0] * n
# for i in range(n-x):
#     dp[i] = sum(visit[i:i+x])
# for i in range(n-x,n):
#     dp[i] = sum(visit[i:])
# max_vis = max(dp)
# ans = 0
# for i in dp:
#     if i == max_vis:
#         ans += 1

# if max_vis == 0:
#     print("SAD")
# else:
#     print(max_vis)
#     print(ans)

