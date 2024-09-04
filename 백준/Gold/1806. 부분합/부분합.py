"""
for문 1개 내에서 끝내야 한다
10000*10000 은 시간초과

누적된 합이 s를 넘을때 마다 시작점을 한칸씩 옮기면서 최소 길이 구한다
"""
import sys
input = sys.stdin.readline

n,s = map(int,input().split())
numlist = list(map(int,input().split()))
total = 0
mini = 1e9
start = 0
for i in range(n):
    total += numlist[i]
    # 합이 s가 될때까지 합친다
    while total >= s:
        # 그때의 최소 거리 구한다
        mini = min(mini,i-start+1)
        # 시작 포인트를 빼준다
        total -= numlist[start]
        # 시작포인트를 옮긴다
        start += 1

if mini == 1e9:
    print(0)
else:
    print(mini)



# 시간 초과 잘못된 풀이
# import sys
# input = sys.stdin.readline
#
# n,s = map(int,input().split())
# numlist = list(map(int,input().split()))
# answerlist = []
# temp = 10000
# for i in range(n):
#     for j in range(n+1):
#         sublist = numlist[i:j]
#         if len(sublist) > temp:
#             continue
#         sub = sum(sublist)
#         if sub >= s:
#             if not answerlist:
#                 answerlist = sublist
#                 temp = len(answerlist)
#             else:
#                 if len(answerlist) > len(sublist):
#                     answerlist = sublist
#                     temp = len(answerlist)
# if answerlist:
#     print(len(answerlist))
# else:
#     print(0)