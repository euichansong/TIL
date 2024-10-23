"""
오목하면 안된다
자기보다 큰거 나올때까지 그 사이 칸 갯수 만큼이 면적

맥스값 기준 반대로 뒤로계산해서 맥스값까지
"""
n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
nlist.sort()

# 최대 높이를 찾고 그 위치를 기억
max_height = 0
max_height_start = 0
max_height_fin = 0
for i in range(n):
    if nlist[i][1] > max_height:
        max_height = nlist[i][1]
        max_height_start = i
        max_height_fin = i
    elif nlist[i][1] == max_height:
        max_height_fin = i

# 면적을 계산하는 부분
answer = 0

# 앞에서부터 최대 높이까지 면적 계산
hei = nlist[0][1]
start_range = nlist[0][0]
for i in range(1, max_height_start + 1):
    if nlist[i][1] > hei:
        answer += (nlist[i][0] - start_range) * hei
        start_range = nlist[i][0]
        hei = nlist[i][1]

# 뒤에서부터 최대 높이까지 면적 계산
b_hei = nlist[-1][1]
b_start_range = nlist[-1][0]
for i in range(n-2, max_height_fin - 1, -1):
    if nlist[i][1] > b_hei:
        answer += (b_start_range - nlist[i][0]) * b_hei
        b_start_range = nlist[i][0]
        b_hei = nlist[i][1]

# 최대 높이 부분의 면적을 더해줌
answer += (nlist[max_height_fin][0] - nlist[max_height_start][0] + 1) * max_height

print(answer)
