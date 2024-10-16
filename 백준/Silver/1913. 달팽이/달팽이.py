"""
n 주니까 n*n 2차원 배열 만들고
중앙부터 채우기 ?

회전은?
기준점 한칸위 언제까지? 현재 진행방향을 숫자로 나타내고 상하좌우에 따라 idx값
# 진행방향
상 0, 우1, 하2, 좌3
중앙점 기준 대각선값이면 방향 변경 이거보단
사용 칸수 다하면 방향 바뀜 이게 낫다
1 1 2 2 3 3 4 4 5 5 6 6
"""

import sys
input = sys.stdin.readline
n = int(input())
need = int(input())
arr = [[0] * n for _ in range(n)]

nowx = n // 2
nowy = n // 2
sn = 1
fn = n ** 2
d = 0

use = 1
next_use = 1
nu = False

while sn <= fn:
    arr[nowx][nowy] = sn
    
    if d == 0:
        nowx -= 1
    elif d == 1:
        nowy += 1
    elif d == 2:
        nowx += 1
    elif d == 3:
        nowy -= 1
    
    use -= 1
    
    if use == 0:
        if nu:
            next_use += 1
        use = next_use
        d = (d + 1) % 4
        nu = not nu
    
    sn += 1

for row in arr:
    print(" ".join(map(str, row)))
for i in range(n):
    for j in range(n):
        if arr[i][j] == need:
            print(i+1,j+1)
