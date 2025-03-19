"""
god good 다른 구성
GOD"과 "GOOD"의 경우 "GOD"에는 'O'가 하나, "GOOD"에는 'O'가 두 개 있으므로 이 둘은 다른 구성을 갖는다.
dog > GOD"에서 'O'를 하나 추가하면 "GOOD" 과 같은 구성을 갖게 되므로 이 둘 또한 비슷한 단어이다.
god good x
dog good o

길이차이 2 이상 나면 다른 단어
같은 길이면 알파벳 갯수 같아야
1 차이 나면 god good x 가지고 있지 않은 다른 문자 더하면 o
    set 했을때 길이가 1차이면 ㅇ? > x


"""
import sys,copy
sys.stdin = open("input.txt")
input = sys.stdin.readline
n = int(input())
fw = list(input().rstrip())
ans = 0
for _ in range(1, n):
    nw = list(input().rstrip())
    # 2글자 이상 차이면 pass
    if abs(len(fw) - len(nw)) >= 2:
        continue
    # 비슷한 문자에서 기준문자 알파벳 하나씩 pop해주고
    else:
        cw = copy.copy(fw)
        f = 0
        flag = True
        # 비슷한지 확인 단어
        for i in nw:
            # 기준 단어
            if cw:
                if i in cw:
                    idx = cw.index(i)
                    cw.pop(idx)
                else:
                    f += 1
            # 기준 단어가 다 pop된 경우
            else:
                break
        if f > 2:
            continue
        # 1글자 차이인 경우
        if len(cw) == 0:
            ans += 1
        elif len(cw) == 1 and f == 1:
            ans += 1

print(ans)
