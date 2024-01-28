def solution(record):
    namedict = {}
    recordlist = []
    for i in record:
        space = list(map(str, i.split()))
        recordlist.append((space[0],space[1]))
        for j in range(len(space)):
            
            if space[0] == 'Enter':
                namedict[space[1]] = space[2]
            elif space[0] == 'Change':
                namedict[space[1]] = space[2]
        
    answer = []
    # for order, id in recordlist: ## 시간초과
    #     if order == 'Enter':
    #         for k, v in namedict.items():
    #             if k == id:
    #                 word = v + '님이 들어왔습니다.'
    #                 answer.append(word)
    #     elif order == 'Leave':
    #         for k, v in namedict.items():
    #             if k == id:
    #                 word = v + '님이 나갔습니다.'
    #                 answer.append(word)
    for order, id in recordlist:
        if order == 'Enter':
            word = namedict[id] + '님이 들어왔습니다.'
            answer.append(word)
        elif order == 'Leave':
            word = namedict[id] + '님이 나갔습니다.'
            answer.append(word)
    # print(answer)
    return answer