t = int(input())
for tc in range(t):
    n = int(input())
    clothdict = {}
    cnt = 1
    for i in range(n):
        cloth, where = input().rstrip().split()
        # clothdict[where] = cnt
        # 옷의 종류 갯수
        if where in clothdict.keys():

            clothdict[where] += 1
        else:
            clothdict[where] = 1
    # print(clothdict)

    combi = 1
    #
    for v in clothdict.values():
        combi *= (v+1)
    # 아무것도 안입는 경우 빼기
    print(combi-1)