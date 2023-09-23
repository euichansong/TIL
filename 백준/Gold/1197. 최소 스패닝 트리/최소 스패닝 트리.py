def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 사이클 발생한다
    if x == y:
        return
    if x < y :
        parents[y] = x
    else:
        parents[x] = y

v, e = map(int, input().split())
edge = []

for _ in range(e):
    a,b,c = map(int, input().split())
    edge.append([a, b, c])
edge.sort(key=lambda x:x[2])
parents = [0] + [i for i in range(1, v+1)]
cnt = 0
sum_w = 0
for f, t, w in edge:
    if find_set(f) != find_set(t):
        cnt += 1
        sum_w += w
        union(f, t)
        if cnt == v:
            break
print(sum_w)