while True:
    g,t,a,d = map(int, input().split())
    if g == -1:
        break
    # g는 그룹의수, t는 각 그룹 구성 팀수, a는 토너먼트로 진출하는 팀의수, d는 조별리그 없이 바로 진출
    # g*a는 조별리그 통과 팀 g*a + d 가 2의 ㅔㅈ곱이 아니면 가까운 2의 제곱팀 추가
    jo = g * a + d

    # 조별리그 경기수 3팀이면 3경기 4팀이면 6경기 3p2
    # ab ac ad bc bd cd 
    pre = t*(t-1)//2 * g
    x = 0
    jegob = 0
    while (2**jegob) < jo:
        x += 2**jegob
        jegob += 1
    x += pre    
    y = 2**jegob - jo
    print(f'{g}*{a}/{t}+{d}={x}+{y}')