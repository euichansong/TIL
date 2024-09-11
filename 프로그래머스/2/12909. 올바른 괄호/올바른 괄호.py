from collections import deque
def solution(s):
    answer = True
    
    q = deque()
    for i in s:
        if i == '(':
            q.append(i)
        else:
            if q:
                q.pop()
            else:
                answer = False
    if q:
        answer = False
    
    return answer