def solution(s):
    # print(list(s))
    # for i in range(len(s)):
    #     if s[i].isdigit():
    #         print(int(s[i]))
    a = list(map(int, s.split()))
    answer = ''
    # print(max(a))
    answer += str(min(a))
    answer += ' '
    answer += str(max(a))
    print(answer)
    
    return answer