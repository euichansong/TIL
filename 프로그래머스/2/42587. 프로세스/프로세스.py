from collections import deque
def solution(priorities, location):
    # answer = 0  왜 1씩 밀리지? 몇번째 실행이라 그런가
    answer = 1
    q = deque(priorities)
    while len(q) > 1:
        now = q.popleft()
        if now < max(q):
            q.append(now)
            if location == 0:
                location = len(q) - 1 # 위치 맨 뒤로 밀린다
            else:
                location -= 1
        else:
            if location == 0:
                return answer
            else:
                answer += 1
                location -= 1
            
    return answer