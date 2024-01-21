def solution(brown, yellow):
    total = brown + yellow
    # print(total)
    answer = []
    
    for se in range(1, (total //2) + 1):
        if total % se == 0:
            ga = total // se
            print(ga,se)
            for i in range(1,ga-1): # 최소 노랑 가로 길이 = 전체 가로 -2
                for j in range(i,se-1): # 최소 노랑 세로 길이 = 전체 세로 -2
                    if i * j == yellow:
                        answer = [se,ga]
    
                        
            
    
    return answer