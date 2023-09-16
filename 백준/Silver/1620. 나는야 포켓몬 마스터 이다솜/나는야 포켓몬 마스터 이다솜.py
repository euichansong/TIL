# 시간초과 코드 index함수의 시간복잡도는 O(n)이기 때문에 시간초과 난다
# import sys
# n, m = map(int, sys.stdin.readline().split())
# polist = [sys.stdin.readline().strip() for _ in range(n)]
#
# problem = [sys.stdin.readline().strip() for _ in range(m)]
# strnum = ['1','2','3','4','5','6','7','8','9']
#
# for i in range(m):
#     if problem[i][0] in strnum:
#     # if problem[i].isdigit():
#         a = problem[i]
#         a = int(a) - 1
#         print(polist[a])
#     else:
#         print(polist.index(problem[i]) + 1)

# 딕셔너리에 저장하는게 해쉬 방식
import sys
n, m = map(int, sys.stdin.readline().split())
podict = {}
for i in range(n):
    poket = sys.stdin.readline().rstrip()
    podict[i+1] = poket
    podict[poket] = i+1
for i in range(m):
    problem = sys.stdin.readline().rstrip()
    if problem.isdigit():
        print(podict[int(problem)])
    else:
        print(podict[problem])