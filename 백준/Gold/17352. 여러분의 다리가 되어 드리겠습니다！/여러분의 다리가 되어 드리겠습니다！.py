import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 주어진 정수n
n = int(input())
# 부모 리스트
parents = [i for i in range(n+1)]

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


for _ in range(n-2):
    a, b = map(int, input().split())
    # 부모가 다르면 합쳐준다
    if find_set(a) != find_set(b):
        union(a, b)
        union(b, a)

# 1부터 n 범위
# for문 끝내기 위한 플래그
for i in range(1, n+1):
    parents[i] = find_set(i)

flag = True
for i in range(1, n+1):
    if flag == False:
        break

    for j in range(i, n+1):
        # 부모가 다르면 출력
        if parents[i] != parents[j]:
            print(i, j)
            flag = False
            break

