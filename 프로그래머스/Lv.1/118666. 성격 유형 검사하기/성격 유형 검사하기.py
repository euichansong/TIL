def solution(survey, choices):
    # print(survey)
    # print(choices)
    answer = ''
    dict = {'R': 0, 'T' : 0, 'C': 0, 'F' : 0, 'J': 0, 'M' : 0, 'A': 0, 'N' : 0}

    for i in range(len(survey)):
        # print(survey[i][0])
        # print(choices[i])
        if choices[i] < 4:
            dict[survey[i][0]] += (4-(choices[i]))
        elif choices[i] > 4:
            dict[survey[i][1]] += (choices[i]%4)
            
            
    if dict['R'] >= dict['T']:
        answer += 'R'
    elif dict['R'] < dict['T']:
        answer += 'T'
        
    if dict['C'] >= dict['F']:
        answer += 'C'
    elif dict['C'] < dict['F']:
        answer += 'F'
        
    if dict['J'] >= dict['M']:
        answer += 'J'
    elif dict['J'] < dict['M']:
        answer += 'M'
        
    if dict['A'] >= dict['N']:
        answer += 'A'
    elif dict['A'] < dict['N']:
        answer += 'N'
    
        
    # print(dict)
    return answer