def solution(s):
    answer = [0,0]
    cnt = 0
    zero = 0
    while s != '1':
        zero += s.count('0')
        a = s.count('1')
        # 이진변환
        two = bin(a)[2:]
        s = two
        cnt += 1
        
    answer[1] = zero
    answer[0] = cnt
    return answer