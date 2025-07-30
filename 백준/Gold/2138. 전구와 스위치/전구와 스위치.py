"""
제한

2 초	128 MB
> for문 1번 가능

문제 해석 

1번은 1,2
나머지는 앞 자신 뒤
n번은 n-1, n 

푸는 방법

000 > 010 3번?

10만 완탐안될듯

1번은 12가 다르면 누름
2번은 123 누를수 있네

n-1번은 n-2,n-1,n
n번은 n-1, n

중간은 같으면 인덱스 추가로 넘어감
끝은 다르면 추가 
다르면 불가능푸는 방법

i-1번째는 i번째 스위치로 변경 가능 
그럼 1번째는? 누른경우 안누른경우 10만 2초니까 가능할듯?
n번쨰는? n번째가 다르면 불가능? >> 아니지 n-1로 n번째 결정하는거니까
"""
import sys
import copy 
n = int(input())
now = list(input())
need = list(input())

now1 = copy.deepcopy(now)
now2 = copy.deepcopy(now)

def change(num):
    if num == '0':
        return '1'
    else:
        return '0'

def light(now,cnt):
    for i in range(1,n):
        # i-1 다르면 i번째 누른다
        if now[i-1] != need[i-1]:
            cnt += 1
            now[i-1] = change(now[i-1])
            now[i] = change(now[i])
            # 마지막 n 이 아니면 i+1까지 
            if i != n-1:
                now[i+1] = change(now[i+1])
    if now == need:
        return cnt
    else:
        return -1

# now1은 첫번째 누른 경우
now1[0] = change(now1[0])
now1[1] = change(now1[1])

aa = light(now1,1)
bb = light(now2,0)
if aa == -1 and bb == -1:
    answer = -1
else:
    if aa > 0 and bb < 0:
        answer = aa
    elif aa < 0 and bb > 0:
        answer = bb
    else:
        answer = min(aa,bb)
print(answer)







