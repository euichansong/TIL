# kruskal 알고리즘
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# find_set 함수
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

# union 함수
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

# 간선 리스트
edge = []
for _ in range(m):
    f, t, w = map(int, input().split())
    edge.append([f, t, w])
# 가중치를 기준으로 오름차순
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


