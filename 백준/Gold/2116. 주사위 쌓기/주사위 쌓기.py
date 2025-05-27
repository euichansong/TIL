"""
2 초	128 MB

af,bd,ce 마주본다

1번주사위 윗면 == 2번주사위 아랫면
1부터 6까지 

주사위갯수 10000?
4개의 옆면 중에서 어느 한 면의 숫자의 합이 최대가 되도록 주사위를 쌓고자 한다 >> 6 아님 5 아님 4
# 잘못된 문제 인식
12 13 14 23 15 24 16 25 34 26 35 36 45 46 56 로 소트? 
a기준 sort pop, 없으면
b기준 sort pop, 없으면
c기준 sort pop?

"""
import sys
input = sys.stdin.readline

n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
# 반대편 인덱스
dict = {0:5,1:3,2:4,3:1,4:2,5:0}
answer = 0

for i in range(6):
    # 현재 주사위 윗면값
    top = dice[0][i]
    # 현재 주사위 아래값
    bottom = dice[0][dict[i]]

    cnt = 0
    if bottom != 6 and top != 6:
        cnt += 6
    elif bottom != 5 and top != 5:
        cnt += 5
    else:
        cnt += 4

    for j in range(1,n):
        # 다음 주사위 인덱스
        nextidx = dice[j].index(top)
        # 다음 주사위 아래값 = 이전주사위 윗면값
        bottom = top
        # 다음주사위 윗면값 = 현재 아래값 반대편
        top = dice[j][dict[nextidx]]

        if bottom != 6 and top != 6:
            cnt += 6
        elif bottom != 5 and top != 5:
            cnt += 5
        else:
            cnt += 4

    answer = max(answer,cnt)
print(answer)        



