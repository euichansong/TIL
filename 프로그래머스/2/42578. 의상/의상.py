def solution(clothes):
    print(clothes)
    answer = 1
    dict ={}
    for v,k in clothes:
        if k in dict.keys():
            dict[k] += 1
        else:
            dict[k] = 1
    
    for v in dict.values():
        answer *= (v+1) # 안입는 경우의 수 추가
    return answer - 1 # 모두 안입은 경우 빼기