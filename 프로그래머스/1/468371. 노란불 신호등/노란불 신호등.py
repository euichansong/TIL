"""
초노빨순
다 초록시작

걍 다 곱해서 같을때 멈춤?
최소공배수까지만 돌아보면 된다
어캐 구함
나눠서 나머지가 그 숫자에 들어가면 그 색깔
"""

def solution(signals):
    # 최대 주기
    total = 1
    answer = -1
    for i in range(len(signals)):
        total *= sum(signals[i])
    print(total)    
    # 시각
    for time in range(1,total+1):
        flag = True
        
        # 노란불 아니면 다음으로 넘어가는게 나을듯
        for g,y,r in signals:
            to = g+y+r
            now = time % to
            if not (g <= now <g+y)  :
                flag = False
                break
                
        if flag:
            answer = time+1
            break
            
    print(answer)
    return answer