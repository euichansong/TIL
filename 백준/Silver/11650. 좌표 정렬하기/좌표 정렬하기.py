import sys

n = int(sys.stdin.readline())
res = []
for i in range(n):
    x, y = map(int,sys.stdin.readline().split())
    res.append([x, y])
res.sort()
# print(res)
for i in res:
    print(*i)