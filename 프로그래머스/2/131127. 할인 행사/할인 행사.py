def solution(want, number, discount):
    answer = 0
    dict = {}
    for i in range(len(want)):
        dict[want[i]] = number[i]
    # 슬라이싱 때문에 1 더해줘야 한다
    for i in range(len(discount)-10+1):
        d2 = dict.copy()
        for key in discount[i:i+10]:
            if key in d2:
                d2[key] -= 1
        cnt = 0
        for v in d2.values():
            if v == 0:
                cnt += 1
        if cnt == len(dict):
            answer += 1
        
    return answer