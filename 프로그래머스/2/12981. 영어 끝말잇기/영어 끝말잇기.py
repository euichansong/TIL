def solution(n, words):
    answer = []
    # word_start = 'words[0][0]'
    # word_end = 'words[0][-1]'
    already = [words[0]]
    cnt = 0
    for i in range(1,len(words)):
        # word_start = words[i][0] # 단어 시작
        # word_end = words[i][-1]  # 단어 끝 >> 다음 단어 시작단어와 일치
        
        if words[i][0] != words[i-1][-1]:
            break
        elif words[i] in already:
            break
        already.append(words[i])
        cnt += 1
    print(cnt)
    if cnt == len(words)-1:
        answer = [0, 0]
    else:
        first = (cnt+1) % n + 1
        second = (cnt+1) // n + 1 
        answer = [first,second]
        
    return answer