import sys
input = sys.stdin.readline

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    elif x < y:
        parents[y] = x
    else:
        parents[x] = y

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    parents = [i for i in range(n+1)]
    cnt = 0
    for _ in range(m):
        a, b = map(int, input().split())
        if find_set(a) != find_set(b):
            union(a, b)
            cnt += 1
    print(cnt)