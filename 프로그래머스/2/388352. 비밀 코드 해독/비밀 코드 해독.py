"""
비밀 코드로 가능한 정수 조합의 갯수

n 최대 숫자 30 까지 
q 입력한 조합
ans 응답 갯수
m ans의 길이
번의 시도

답이 0인건 없다

정수조합이면 완탐?

ans의 크기가 큰 순서대로 정렬을 하면 ? 
작은순서대로 해서 숫자를 뺀다?

30c 5니까 142,506 완탐이네

응답 0인거 빼기
"""
from itertools import combinations
def solution(n, q, ans):
    answer = 0
    # 응답 없는 숫자 제거
    delete = []
    for i in range(len(q)):
        if ans[i] == 0:
            for j in range(5):
                if q[i][j] not in delete:
                    delete.append(q[i][j])
    # 가능한 숫자
    num = []
    for i in range(1,n+1):
        if i not in delete:
            num.append(i)
    l = list(combinations(num,5))
    # 조합마다 돌면서 
    for i in l:
        flag = True
        # q 돌면서 
        for j in range(len(q)):
            cnt = 0
            # q의 숫자 돌면서 
            for k in range(5):
                # q안의 숫자가 l에 있으면 cnt += 1
                if q[j][k] in i:
                    cnt += 1
            # cnt 같으면 가능한 조합
            if cnt != ans[j]:
                flag = False
                break
        if flag:
            answer += 1    
    return answer




