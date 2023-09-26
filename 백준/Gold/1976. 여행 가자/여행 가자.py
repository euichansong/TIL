# find_set 함수
def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


# 유니온 함수
def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


n = int(input())
m = int(input())
parents = [i for i in range(n+1)]
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            for kk in range(2):
                union(i + 1, j + 1)
                union(j + 1, i + 1)
plan_list = list(map(int, input().split()))
res = []
for q in plan_list:
    res.append(find_set(q))

if len(list(set(res))) == 1:
    print('YES')
else:
    print('NO')
