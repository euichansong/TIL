"""
틀린 방식 
같은 대기 시간에 여러 작업이 있는 경우 생각 안했네;

import heapq
def solution(jobs):
    answer = 0
    q = []
    # 작업 힙큐에 넣는다
    for i in jobs:
        heapq.heappush(q,(i[1],i[0]))
    # print(q)
    time = 0
    while q:
        # 시간 1 주기위해 if문 만듬
        if len(q) > 0:
            # 대기시간 순으로 정렬된 q를 뽑는다
            work, wait = heapq.heappop(q)
            print(work, wait)
            print(time)
            # 작업시간에 pop한 작업시간 추가
            time += work
            # 정답에 더한 시간에서 기다리는 시간 뺀 값 더해준다
            answer += (time - wait)
        else:
            time += 1
        print(answer)
        print(time)
    answer = answer // len(jobs)
    return answer
"""
import heapq
def solution(jobs):
    answer = 0
    q = []
    time = 0
    cnt = 0
    # 0으로 놓고 이상으로 범위 설정하면 안된다 
    start = -1
    while cnt < len(jobs):
        # 작업 힙큐에 넣는다
        for i in jobs:
            # 현재 시간보다 작은 것만
            # 시작시간보다 큰거만
            if start < i[0] <= time:
                heapq.heappush(q,(i[1],i[0]))

        # 시간 1 주기위해 if문 만듬
        if len(q) > 0:
            # 대기시간 순으로 정렬된 q를 뽑는다
            work, wait = heapq.heappop(q)
            # 시작시간을 현재 시간으로 
            start = time
            # 작업시간에 pop한 작업시간 추가
            time += work
            # 정답에 요청부터 종료까지 시간 추가
            answer += (time - wait)
            cnt += 1
        else:
            time += 1

    answer = answer // len(jobs)
    return answer

jobs = [[0, 3], [1, 9], [2, 6]]
solution(jobs)