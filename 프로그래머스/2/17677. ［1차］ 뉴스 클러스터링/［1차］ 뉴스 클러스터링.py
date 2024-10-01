def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ts1 = []
    ts2 = []
    for i in range(len(str1)-1):
        s = str1[i:i+2]
        al = True
        for j in s:
            if j not in alpha:
                al = False
                break
        if al:
            ts1.append(s)
            
    for i in range(len(str2)-1):
        s = str2[i:i+2]
        al = True
        for j in s:
            if j not in alpha:
                al = False
                break
        if al:
            ts2.append(s)    
    hab = 0
    gyo = 0
    
    for i in ts1:
        if i in ts2:
            gyo += 1
        else:
            hab += 1
            
    # 자카드 유사도 구하기
    if len(ts1) == 0 and len(ts2) == 0:
        j = 1
    else:
        # 다중합집합
        a_temp = ts1.copy()
        a_result = ts1.copy()
        for i in ts2:
            if i not in a_temp: # B에만 존재하면 합집합에 추가
                a_result.append(i) 
            else: # 공통으로 존재하면 중복되므로 제거
                a_temp.remove(i)
        # 다중교집합
        result = []
        for i in ts2:
            if i in ts1:
                ts1.remove(i)
                result.append(i)

        j = len(result)/len(a_result) # 자카드 유사도 = 교집합/합집합
        
    return (int(j * 65536))