import sys
n = int(sys.stdin.readline())
cnt = 0
res = []

for _ in range(n):
    agename = list(sys.stdin.readline().split())
    # 숫자로 받기
    agename[0] = int(agename[0])
    # 순서 세기 위해
    res.append(agename + [cnt])
    cnt += 1
    # q.append(agename)
# 나이 오름차순
res.sort(key = lambda x: x[0])
for i in range(n):
    print(res[i][0], ''.join(res[i][1]))