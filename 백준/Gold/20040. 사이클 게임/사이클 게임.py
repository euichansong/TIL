import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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


n, m = map(int, input().split())
parents = [k for k in range(n)]
flag = True
cnt = 1
for i in range(m):
    a, b = map(int, input().split())
    aa = find_set(a)
    bb = find_set(b)
    if aa != bb:
        union(a, b)
    else:
        print(cnt)
        flag = False
        break
    cnt += 1
if flag == True:
    print(0)
