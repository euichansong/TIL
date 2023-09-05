import sys
# 후보
n = int(sys.stdin.readline())
# 투표 명단
nlist = []
# 다솜이 찍은 사람
first = int(sys.stdin.readline())

cnt = 0
# 투표명단 리스트에 넣고 내림차순 정렬
for _ in range(1,n):
    a = int(sys.stdin.readline())
    nlist.append(a)
nlist.sort(reverse=True)
# 투표인원 1명이면 답 0
if n == 1:
    print(0)
else:
    # 투표 명단이 다솜이 찍은사람보다 클때까지 반복
    while nlist[0] >= first:
        nlist[0] -= 1
        first += 1
        cnt += 1
        # 매수하면 다시 내림차순 정렬
        nlist.sort(reverse=True)
    print(cnt)