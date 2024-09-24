from collections import deque

def find_gual(s):
    q = []
    if s[0] == '}' or s[0] == ']' or s[0] == ')' or (len(s) % 2 == 1):
        return False
    for i in s:
        if i == '[':
            q.append(i)
        elif i == ']':
            if q and q[-1] == '[':
                q.pop()
            else:
                return False
        if i == '(':
            q.append(i)
        elif i == ')':
            if q and q[-1] == '(':
                q.pop()
            else:
                return False
        if i == '{':
            q.append(i)
        elif i == '}':
            if q and q[-1] == '{':
                q.pop()
            else:
                return False
    return True

def solution(s):
    answer = 0
    s = deque(list(s))
    cnt = 0
    while cnt < len(s):
        if find_gual(s):
            answer += 1
        t = s.popleft()
        s.append(t)
        cnt += 1
    return answer

s = "}]()[{"
solution(s)