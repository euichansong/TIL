def solution(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].capitalize()
        print(s[i])
    answer = ' '.join(s)
    return answer

"""
날먹 실패
answer = s.capitalize()
answer = answer.title()
=======================
44%
def solution(s):
    answer = ''
    s = list(s.split())
    for i in s:
        find = list(i)
        if i == s[-1]:
            if find[0].isdigit():
                answer += i.lower()
            else:
                answer += i.title()
        else:
            if find[0].isdigit():
                answer += i.lower()
            else:
                answer += i.title()
            answer += ' '
    print(answer)
    return answer
"""