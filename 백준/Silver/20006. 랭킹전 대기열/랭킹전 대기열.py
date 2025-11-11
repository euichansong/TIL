"""
1 초	256 MB

매칭 없으면 새로운방
처음입장렙 기준 +-10

입장가능방 있으면 정원 찰때까지 대기
    여러개면 먼저생성
입력된 순서대로 게임을 시작한다.

딕셔너리? 키밸류 방 
>>> 실패 이유는 다 같은 레벨일때 방이 차있으면 덮힌다
>> 키값을 키,네임 튜플로 변경
"""
p,m = map(int, input().split())
player = [list(input().split()) for _ in range(p)]

dict = {(int(player[0][0]),player[0][1]):[[int(player[0][0]),player[0][1]]]}

for i in range(1,p):
    lev = int(player[i][0])
    name = player[i][1]
    # dict에 입장가능한 방이 있는지
    flag = True
    for j,na in dict.keys():
        # 한번 입장하면 끝
        if flag:
            # 범위내에
            j = int(j) 
            if (lev >= (j - 10)) and (lev <= (j + 10)):
                # 정원내에
                if len(dict[(j,na)]) < m:
                    dict[(j,na)].append([lev,name])
                    flag = False
                    break
    # 입장 가능한 방이 없다면 생성
    else:
        dict[(lev,name)] = [[lev,name]]

for k in dict.keys():
    if len(dict[k]) == m:
        print('Started!')
        sp = sorted(dict[k], key=lambda x: x[1])
        for v in sp:
            print(*v)
    else:
        print('Waiting!')
        sp = sorted(dict[k], key=lambda x: x[1])
        for v in sp:
            print(*v)
