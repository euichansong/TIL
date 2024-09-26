import math

def solution(progresses, speeds):
    answer = []
    lp = len(progresses)
    dev = []
    for i in range(lp):
        p = math.ceil((100 - progresses[i]) / speeds[i])  # 올림 처리
        dev.append(p)
        
    idx= 0
    cnt = 1
    for i in range(1,len(dev)):
        if dev[idx] >= dev[i]:
            cnt += 1
        else:
            answer.append(cnt)
            idx = i
            cnt = 1
    answer.append(cnt)
    
    return answer