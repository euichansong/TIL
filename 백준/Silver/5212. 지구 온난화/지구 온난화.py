from copy import deepcopy


R, C = map(int,input().split())
di = [1,0,-1,0]
dj = [0,-1,0,1]
land = []
lastland_i = []
lastland_j = []
sea = [ list(input()) for _ in range(R)]
newsea = deepcopy(sea)
for i in range(R):
    for j in range(C):
        if sea[i][j] == 'X':
            land.append([i,j])

for k in land:
    ki = k[0]
    kj = k[1]
    cnt = 0
    for l in range(4):
        next_i = ki + di[l]
        next_j = kj + dj[l]
        if 0 > next_i or next_i >= R or 0 > next_j or next_j >= C :
            cnt+=1
        elif sea[next_i][next_j] == ".":
            cnt+=1

    if cnt>=3:
        newsea[ki][kj] = '.'
        cnt = 0
    else:
        lastland_i.append(ki)
        lastland_j.append(kj)

lastland_i.sort()
lastland_j.sort()
start_i = lastland_i[0]
end_i = lastland_i[-1]
start_j = lastland_j[0]
end_j = lastland_j[-1]
for n in range(start_i,end_i+1):
    print(''.join(newsea[n][start_j:end_j+1]))

