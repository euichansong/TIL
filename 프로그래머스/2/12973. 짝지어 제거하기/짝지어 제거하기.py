def solution(s):
    answer = -1
    q = []
    for i in range(len(s)):
        if not q:
            q.append(s[i])
        else:
            if s[i] == q[-1]:
                q.pop()
            else:
                q.append(s[i])
    if q:
        answer = 0
    else:
        answer = 1
        
    
    
    return answer