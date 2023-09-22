# kruskal 알고리즘

n = int(input())
m = int(input())


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


edge = []
for _ in range(m):
    f, t, w = map(int, input().split())
    edge.append([f, t, w])
edge.sort(key=lambda x: x[2])
parents = [i for i in range(n+1)]
cnt = 0
sum_w = 0
for f1,t1,w1 in edge:
    if find_set(f1) != find_set(t1):
        cnt += 1
        sum_w += w1
        union(f1, t1)
        if cnt == n:
            break
print(sum_w)


