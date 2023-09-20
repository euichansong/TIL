t = int(input())
for tc in range(t):
    n = int(input())
    clothdict = {}
    for i in range(n):
        cloth, where = input().rstrip().split()
        # 옷의 종류 갯수세기 없으면 1로 시작
        if where in clothdict.keys():
            clothdict[where] += 1
        else:
            clothdict[where] = 1
    # print(clothdict)

    combi = 1
    #
    for v in clothdict.values():
        # 모든 종류의 의류 입지 않는 경우 포함
        combi *= (v+1)
    # 아무것도 안입는 경우 빼기
    print(combi-1)
