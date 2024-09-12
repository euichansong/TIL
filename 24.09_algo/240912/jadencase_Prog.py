"""
날먹 실패
answer = s.capitalize()
answer = answer.title()
"""


"""
title 안되네
split() 랑 split('') 는 다른것이다
"""
def solution(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    answer = ' '.join(s)
    return answer

s = "3people unFollowed me"
solution(s)