"""
id, 문제번호, 점수

여러번 가능하고 최고점수가 최종
제출 안하면 0점

같은 점수면 풀이 제출회수 적은순
마지막 제출시간 빠른순

순위 출력
최종 점수는 각 문제에 대해 받은 점수의 총합이고, 당신의 순위는 (당신 팀보다 높은 점수를 받은 팀의 수)+1
"""
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    # 팀 갯수, 문제 갯수, 팀 ID, 로그 갯수
    n, k, t, m = map(int, input().split())
    # 팀 [최종 점수, 제출 횟수, 마지막 제출 시간]
    team = [[0, 0, 0] for _ in range(n + 1)]
    # 문제별[각문제][팀점수]
    problem = [[0] * (n + 1) for _ in range(k)]

    for mm in range(m):
        # 팀 ID, 문제 번호, 점수
        tid, pnum, score = map(int, input().split())
        # idx 맞추기
        pnum -= 1
        # 점수 갱신
        if score > problem[pnum][tid]:
            # 현재 점수에 갱신점수 - 기존점수 추가
            team[tid][0] += score - problem[pnum][tid]
            problem[pnum][tid] = score
        # 횟수 증가
        team[tid][1] += 1
        # 마지막 제출
        team[tid][2] = mm

    # 본인 팀 정보
    ourt = team[t]
    # 순위 계산
    rank = 1
    for i in range(1, n + 1):
        if i == t:
            continue
        if team[i][0] > ourt[0]:
            rank += 1
        elif team[i][0] == ourt[0]:
            if team[i][1] < ourt[1]:
                rank += 1
            elif team[i][1] == ourt[1]:
                if team[i][2] < ourt[2]:
                    rank += 1

    print(rank)


        
