"""
역순 ?
5에서 12 가는 경우 +1 x2 / x2 +1 +1
17 16 8 4 5
5 24
24 12 6 5
5 25
25 24 12 6 5
이분탐색 dp 아니야?

"""
from collections import deque
n, k = map(int, input().split())


max_cnt = 0
def bfs(start, cnt, k):

    global max_cnt
    q = deque()
    q.append([start,cnt])
    dp = [0] * 100002
    dp[start] = 1
    while q:
        ns, ncnt = q.popleft()
        if ns == k:
            return ncnt
            # if max_cnt < ncnt:
            #     ncnt = max_cnt
        for next in [ns+1, ns-1, ns*2]:
            if 0 <= next <= 100000 and dp[next] == 0:
                q.append([next, ncnt + 1])
                dp[next] = 1



print(bfs(n,0, k))
# print(max_cnt)