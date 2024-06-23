"""
5 7 4 2 2
3 2
1 1 3
2 3 5
3 5 1
4 4 4

n,m,p,c,d
n = 판의 크기
m = 턴 수
p = 산타 수
c = 루돌프가 움직여서 충돌시 얻는 점수 + 루돌프가 이동해온 방향으로 밀려남
d = 산타가 움직여서 충돌시 얻는 점수 + 산타가 이동한 방향 반대로 밀려남

"""
n,m,p,c,d = map(int, input().split())
rr, rc = map(int, input().split())
# 앞에는 값 뒤에는 기절 여부
# 기절시 -2 넣고 턴 끝나면 + 1 해주기
# r값, c값, 기절여부, 탈락여부, 값
santalist = [[0,0,0,0,0] for _ in range(p+1)]

mapcode = [[0] * (n+1) for _ in range(n+1)]
mapcode[rr][rc] = -1
near_santa = 0
near_ru_san = 0
r_san = 0
c_san = 0

for i in range(p):
    pn, sr, sc = map(int, input().split())
    mapcode[sr][sc] = pn
    santalist[pn][0] = sr
    santalist[pn][1] = sc
    ru_len = (sr-rr)**2 + (sc-rc)**2
    if near_ru_san < ru_len:
        near_ru_san = ru_len
        near_santa = pn
        r_san = sr
        c_san = sc
    elif near_ru_san == ru_len:
        if r_san < sr:
            near_santa = pn
            r_san = sr
            c_san = sc
        elif r_san == sr:
            if c_san < sc:
                near_santa = pn
                r_san = sr
                c_san = sc
            elif c_san > sc:
                pass

        else:
            pass
    else:
        pass

# 대각선 움직임 가능
mx = [-1,-1,-1,0,0,0,1,1,1]
my = [-1,0,1,-1,0,1,-1,0,1]
# 산타 움직임 가능
sx = [-1,0,1,0]
sy = [0,1,0,-1]
print(near_santa)
print(r_san,c_san)


for i in mapcode:
    print(i)