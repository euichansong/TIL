def solution(k, tangerine):
    answer = 0
    dict = {}
    for i in tangerine:
        if i not in dict:
            dict.setdefault(i,1)
        else:
            dict[i] += 1
    # value값으로 내림차순 정렬
    dict = sorted(dict.items(), key=lambda x : x[1] , reverse=True)
    cnt = 0
    for key,value in dict:
        cnt += value
        answer += 1
        if cnt >= k:
            break
    return answer