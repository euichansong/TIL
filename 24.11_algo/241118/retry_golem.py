"""
우선순위
1. 남쪽 1칸 - 밑에 아무것도 없을때 이동
2. 서쪽으로 회전 - 옆에 이동 가능할때, 출구 방향 변경
3. 동쪽으로 회전 - 옆에 이동 가능할때, 출구 방향 변경
0,1,2,3은 북, 동, 남, 서
4. 최대 이동시 숲 벗어나면 숲 초기화

이동할수 없으면 골렘 이동 가능, 골렘 출구로 나가야 한다

6 5 6
2 3
2 0
4 2
2 0
2 0
2 2

지금 상황
회전이 안되고 있다
"""
def push_gorem(direct, gorembottom):
    maplist[gorembottom][start] = 1
    # 출구가 상
    if direct == 0:
        # 상
        maplist[gorembottom-1][start] = 9
        # 좌
        maplist[gorembottom][start-1] = 1
        # 우
        maplist[gorembottom][start + 1] = 1
        # 하
        maplist[gorembottom + 1][start] = 1
    # 출구가 우
    elif direct == 1:
        # 상
        maplist[gorembottom-1][start] = 1
        # 좌
        maplist[gorembottom][start-1] = 1
        # 우
        maplist[gorembottom][start + 1] = 9
        # 하
        maplist[gorembottom + 1][start] = 1
    # 출구가 하
    elif direct == 2:
        # 상
        maplist[gorembottom - 1][start] = 1
        # 좌
        maplist[gorembottom][start - 1] = 1
        # 우
        maplist[gorembottom][start + 1] = 1
        # 하
        maplist[gorembottom + 1][start] = 9
    # 출구가 좌
    elif direct == 3:
        # 상
        maplist[gorembottom - 1][start] = 1
        # 좌
        maplist[gorembottom][start - 1] = 9
        # 우
        maplist[gorembottom][start + 1] = 1
        # 하
        maplist[gorembottom + 1][start] = 1



r, c, k = map(int, input().split())
maplist = [[0] * c for _ in range(r)]  # 숲 초기화

for _ in range(k):
    start, direct = map(int, input().split())
    start -= 1  # 0-indexed로 변환
    bottem_temp = 0
    can_move = False

    for gorembottom in range(r-2):  # 골렘이 내려가는 루프
        can_move = False  # 초기화

        # 1. 남쪽으로 이동 가능 (중앙과 양옆 검사)
        if (gorembottom + 1 < r and
            maplist[gorembottom+1][start] == 0 and
            start - 1 >= 0 and maplist[gorembottom+1][start-1] == 0 and
            start + 1 < c and maplist[gorembottom+1][start+1] == 0
        ):
            bottem_temp = gorembottom + 1
            can_move = True
            continue

        # 2. 서쪽으로 회전 가능 (왼쪽 아래와 왼쪽 위 검사)
        if (
            start - 1 >= 0 and
            gorembottom + 1 < r and
            maplist[gorembottom+1][start-1] == 0 and
            maplist[gorembottom][start-1] == 0
        ):
            direct = (direct + 1) % 4  # 반시계 방향 회전
            start -= 1
            bottem_temp = gorembottom + 1
            can_move = True
            continue

        # 3. 동쪽으로 회전 가능 (오른쪽 아래와 오른쪽 위 검사)
        if (
            start + 1 < c and
            gorembottom + 1 < r and
            maplist[gorembottom+1][start+1] == 0 and
            maplist[gorembottom][start+1] == 0
        ):
            direct = (direct - 1) % 4  # 시계 방향 회전
            start += 1
            bottem_temp = gorembottom + 1
            can_move = True
            continue

        # 4. 이동 및 회전 불가 -> 루프 종료
        break

    if bottem_temp == r-2:
        can_move = False
    # 모든 이동 및 회전이 불가능한 경우 push_gorem 호출
    if not can_move:
        push_gorem(direct, bottem_temp)

    # 디버깅용 출력
    for row in maplist:
        print(row)
    print("================")