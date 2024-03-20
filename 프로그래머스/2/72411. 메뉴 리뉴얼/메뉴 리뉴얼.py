"""
해쉬 같은데 딕셔너리?
완탐일까?
코스가 가능한 조합갯수 보여준다고 생각?
"""
from itertools import combinations
def solution(orders, course):
    dict = {}
    # 단어 자르기
    for i in orders:
        slice = []
        for j in range(len(i)):
            slice.append(i[j])
        slice.sort()
        # 조합 만들기
        for c in course:
            combi = list(combinations(slice,c))
            # 딕셔너리 저장
            for com in combi:
                if com in dict:
                    dict[com] += 1
                dict.setdefault(com,1)
    answer = []
    bb = max(course)
    # 정답 배열
    answerlist = [[] for _ in range(bb+1)]
    # 코스별 길이 
    for c in course:
        maxcount = 0
        for key, value in dict.items():
		        # 길이가 코스와 같고, 2개 이상
            if len(key) == c and value >= 2:                       
                if value > maxcount:
                    answerlist[c] = []
                    answerlist[c].append(key)
                    maxcount = value
                elif value == maxcount:
                    answerlist[c].append(key)
                    maxcount = value
    # 다시 합치기 (튜플상태 이기 때문)
    for c in course:
        for w in answerlist[c]:
            word = ''
            for www in w:
                word += www
            answer.append(word)
    answer.sort()
    return answer