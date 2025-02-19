"""
god good 다른 구성
GOD"과 "GOOD"의 경우 "GOD"에는 'O'가 하나, "GOOD"에는 'O'가 두 개 있으므로 이 둘은 다른 구성을 갖는다.
dog > GOD"에서 'O'를 하나 추가하면 "GOOD" 과 같은 구성을 갖게 되므로 이 둘 또한 비슷한 단어이다.
god good x
dog good o

길이차이 2 이상 나면 다른 단어
같은 길이면 알파벳 갯수 같아야
1 차이 나면 god good x 가지고 있지 않은 다른 문자 더하면 o
    set 했을때 길이가 1차이면 ㅇ?
"""
import sys,copy
sys.stdin = open("input.txt")
input = sys.stdin.readline
n = int(input())
fw = list(input().rstrip())
ans = 0
for _ in range(1,n):
    nw = list(input().rstrip())
    if abs(len(fw)-len(nw)) >= 2:
        continue
    # 길이 같은 경우 문자 갯수 같은지
    if len(fw) - len(nw) == 0:
        aa = list(set(fw))
        bb = list(set(nw))
        if aa == bb:
            ans += 1
            continue
        elif len(aa) - len(bb) == 1:
            ans += 1
            continue


    # fw가 짧은경우
    if len(fw) -len(nw) == -1:
        for i in fw:
            if i in nw:
                idx = nw.index(i)
                nw.pop(idx)
        if len(nw) == 1:
            ans += 1
    # fw가 긴경우
    if len(fw) -len(nw) == 1:
        cow = fw.copy()
        for i in nw:
            if i in cow:
                idx = cow.index(i)
                cow.pop(idx)
        if len(cow) == 1:
            ans += 1
print(ans)
