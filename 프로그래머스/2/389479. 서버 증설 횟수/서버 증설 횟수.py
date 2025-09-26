"""
n = 현재 서버 갯수
m = 서버 증설해야하는 인원
k = 서버 유지 시간

> 서버 1개 있다고 생각하고 시작

일단 그리디로 생각하자

큐를 만들어서 [추가한 서버,서버유지시간k] 이렇게 넣고 큐 다 돌면서 시간을 뺀다 
"""
from collections import deque
def solution(players, m, k):
    answer = 0
    server = 0
    q = deque()
    for i in range(len(players)):
        
        # print(i,"현재시간")
        # 필요한 서버 숫자
        need = players[i] // m
        # 필요한 서버 숫자가 현재 서버보다 작으면 패스
        if need > server:
            add = need - server
            server += add
            answer += add
            q.append([add, k])
            # print(need,"서버추가",server,"현재서버")
        # print("===================")
        
        # 서버 유지시간 빼기
        for _ in range(len(q)):
            s, t = q.popleft()
            t -= 1
            if t == 0:
                server -= s
            else:
                q.append([s, t])  
              
    return answer