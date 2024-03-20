"""
해쉬 같은데 딕셔너리?
완탐일까?
코스가 가능한 조합갯수 보여준다고 생각?
"""
from itertools import combinations
def solution(orders, course):
    dict = {}
    for i in orders:
        slice = []
        for j in range(len(i)):
            slice.append(i[j])
        slice.sort()
        for c in course:
            combi = list(combinations(slice,c))
            for com in combi:
                if com in dict:
                    dict[com] += 1
                dict.setdefault(com,1)
    answer = []
    bb = max(course)
    answerlist = [[] for _ in range(bb+1)]
    
    for c in course:
        maxcount = 0
        for key, value in dict.items():
            if len(key) == c and value >= 2:                       
                if value > maxcount:
                    answerlist[c] = []
                    answerlist[c].append(key)
                    maxcount = value
                elif value == maxcount:
                    answerlist[c].append(key)
                    maxcount = value
    print(answerlist)
    
    for c in course:
        
        print(answerlist[c])
        for w in answerlist[c]:
            word = ''
            for www in w:
                word += www
            print(word)

            answer.append(word)
    answer.sort()
    print(answer)
    
    return answer