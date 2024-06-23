"""
6 5 6
2 3
2 0
4 2
2 0
2 0
2 2
"""

"""
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
"""
시작열, 출구방향
0북 1동 2남 3서
"""
maplist = [[0] * (c+1) for _ in range(r+1)]

for _ in range(k):
    start, direct = map(int, input().split())
    bottem_temp = 0
    for gorembottom in range(1,r):
        if maplist[gorembottom+1][start]==0:
            bottem_temp = gorembottom
            continue
        # 밑바닥에 부딪힐때
        elif maplist[gorembottom+1][start] != 0:
            # 왼쪽으로 구를 수 있는 경우
            if maplist[gorembottom+1][start-1] == 0:
                # 그만 구르는 경우
                if start == 2:
                    bottem_temp = gorembottom
                    push_gorem(direct,bottem_temp)
                    break
                else:
                    # 더 구를수 있는 경우
                    # 방향 -1, start -1
                    if direct == 3:
                        direct = 0
                    else:
                        direct += 1
                    start -= 1
            # 오른쪽으로 구를 수 있는 경우
            elif maplist[gorembottom+1][start+1] == 0:


                # 그만 구르는 경우
                if start == c-2:
                    bottem_temp = gorembottom
                    push_gorem(direct, bottem_temp)
                    break
                else:
                    # 더 구를수 있는 경우
                    # 방향 + 1, start + 1
                    if direct == 0:
                        direct = 3
                    else:
                        direct -= 1
                    start += 1
            # 못가는 경우
            else:
                push_gorem(direct, bottem_temp)
                break

    if bottem_temp == r-1:
        push_gorem(direct,bottem_temp)
    for i in maplist:
        print(i)
    print("================")