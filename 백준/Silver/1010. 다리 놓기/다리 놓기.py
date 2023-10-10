# ==========================
# 시간초과
# import itertools, sys
# input = sys.stdin.readline
# t = int(input())
# for tc in range(1, t+1):
#     a, b = map(int, input().split())
#     res = len(list(itertools.combinations(range(1,b+1), a)))
#     print(res)
import sys
input = sys.stdin.readline
t = int(input())
for tc in range(1, t+1):
    a, b = map(int, input().split())
    top = 1
    for i in range(b, b-a, -1):
        top *= i
    bottom = 1
    for w in range(1, a+1):
        bottom *= w
    print(int(top//bottom))