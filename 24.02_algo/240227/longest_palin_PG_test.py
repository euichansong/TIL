"""
중간값 어떻게 잡지?
중간값 기준 옆으로 하나씩 보면서 같은지 비교하는 함수 만들기?
"""


def solution(s):
    answer = 0
    s = list(s)
    for mid in range(1, len(s)):
        res = palin(s, mid)
        if answer < res:
            answer = res
    return answer


def palin(list, mid):
    add = 0
    flag = True
    while flag:
        if 0 <= (mid - add) and (mid + add) < len(list):
            if list[mid - add] == list[mid + add]:
                add += 1
            else:
                flag = False
        else:
            flag = False
    return (2 * add) - 1

s = 'abcdcba'
print(solution(s))