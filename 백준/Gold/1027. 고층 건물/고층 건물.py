"""
2 초	128 MB

N은 50보다 작거나 같은 자연수
A에서 B가 볼 수 있는 빌딩이 되려면, 두 지붕을 잇는 선분이 A와 B를 제외한 다른 빌딩을 지나거나 접하지 않아야 한다.

7에서 6 6 4 2  3 1 5 >> 기울기가 겹치면 안된다

> 오른쪽 건물들은 기울기가 커야 보인다
> 왼쪽 건물은 기울기가 작아야 보인다
"""
n = int(input())
nlist = list(map(int, input().split()))
answer = 0
for i in range(n):
    # 오른쪽 건물은 기울기가 커야 보인다
    max_gi = -1e9
    right_cnt = 0
    for j in range(i+1,n):
        gi = (nlist[j]-nlist[i])/(j-i)
        if gi > max_gi:
            right_cnt += 1
            max_gi = gi

    # 왼쪽 건물은 기울기가 작아야 보인다
    min_gi = 1e9
    left_cnt = 0
    for j in range(i-1,-1,-1):
        gi = (nlist[j]-nlist[i])/(j-i)
        if gi < min_gi:
            left_cnt += 1
            min_gi = gi

    answer = max(answer, left_cnt + right_cnt)
print(answer)

