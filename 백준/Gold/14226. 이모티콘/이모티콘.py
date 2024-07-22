"""
2배 되기도 하고  2초
1개 삭제 가능하고  1초
1000이니까 백트레킹 힘들거 같은데

bfs 돌려서 기존보다 작으면 브래이크

클립보드에 복사하고 나중에 사용 사능
"""
import sys
input = sys.stdin.readline

from collections import deque

def bfs(num,dp):
    q = deque()
    # 시작숫자, 카운트, 클립보드이모지 갯수
    q.append([1,0,0])
    while q:
        next, ncnt, nemo = q.popleft()
        if next == num:
            print(ncnt)
            break
        # for nt, nc, ne in [[next, ncnt+1, next],
        #                   [next+nemo, ncnt+1, nemo],
        #                   [next-1, ncnt+1, nemo]]:
        #     if 0 < nt <= (num*2) and nc <= dp[nt]:
        #         dp[nt] = nc
        #         q.append([nt,nc,ne])
        for i in range(3):

            # 1. 복사후 저장
            if i == 0:
                nt, nc, ne = next, ncnt+1, next
            # 2. 붙여넣기
            elif i == 1:
                if nemo == 0:
                    continue
                nt, nc, ne = next + nemo, ncnt + 1, nemo
            # 3. 화면에 있는 이모지 하나 삭제
            else:
                nt, nc, ne = next-1, ncnt+1, nemo
            if 0 < nt <= 1000 and  0 <= ne <= 1000 and dp[nt][ne] == 0:
                if dp[nt][ne] > nc:
                    continue
                dp[nt][ne] = nc
                q.append([nt, nc, ne])
num = int(input())
dp = [[0] * 1001 for _ in range(1001)]
bfs(num,dp)
