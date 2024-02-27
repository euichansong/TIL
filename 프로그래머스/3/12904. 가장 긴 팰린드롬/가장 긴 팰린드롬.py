"""
중간값 어떻게 잡지?
중간값 기준 옆으로 하나씩 보면서 같은지 비교하는 함수 만들기?
+++
짝수 펠린드롬 생각해야 했다
"abba"
"""
def solution(s):
    answer = 0
    s = list(s)
    for mid in range(len(s)):
        # 펠린드롬 홀수 경우
        res_odd = palin(s, mid, mid)
        # 펠린드롬 짝수 경우
        res_even = palin(s, mid, mid+1)
        # 가장 큰 값
        answer = max(res_odd, res_even, answer)
    # 가장 긴 길이가 1인 경우    
    if answer <= 0:
        answer = 1
    return answer

def palin(list, left, right):
    while 0 <= left and right < len(list) and list[left] == list[right]:
        left -= 1
        right += 1

    return right - left - 1
        