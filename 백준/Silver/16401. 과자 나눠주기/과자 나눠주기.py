"""

과자의 길이가 같아야 한다

과자의 길이는 snack
과자는 길이와 상관없이 여러조각으로 나뉠수 있다.

예1 8 8 8 
예2 7 7 7+7 
"""

import sys
input = sys.stdin.readline
# 조카 m 과자 n
m,n = map(int, input().split())
snack = list(map(int, input().split()))
snack.sort(reverse=True)

l = 1
r = max(snack)

while l <= r:
    mid = (l+r) // 2
    cnt = 0
    for s in snack:
        # 나눌수 있는 사람
        cnt += s // mid
        if cnt >= m:
            break
    # 길이 늘이기
    if cnt >= m:
        l = mid + 1
    # 길이 줄이기
    else:
        r = mid -1

print(r)








