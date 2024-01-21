def solution(brown, yellow):
    total = brown + yellow
    # print(total)
    answer = []
    
    for se in range(1, (total //2) + 1):
        if total % se == 0:
            ga = total // se
            print(ga,se)
            for i in range(1,ga-1):
                for j in range(i,se-1):
                    if i * j == yellow:
                        answer = [se,ga]
    
                        
            
    
    return answer