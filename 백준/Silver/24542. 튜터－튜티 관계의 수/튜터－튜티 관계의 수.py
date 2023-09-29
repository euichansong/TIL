import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# find_set함수
def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

# union함수
def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    elif x < y:
        parents[y] = x
    else:
        parents[x] = y

n, m = map(int, input().split())
parents = [q for q in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    if find_set(u) != find_set(v):
        union(u, v)
for k in range(n+1):
    parents[k] = find_set(k)

parents = parents[1:]
set_list = list(map(str, set(parents)))
count = [0]*(n+1)
for i in parents:
    count[i] += 1
# print(parents)
# print(count)
res = 1
for i in count:
    if i != 0:
        res *= i
print(res % 1000000007)