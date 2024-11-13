import sys
# from collections import deque
input = sys.stdin.readline

k,l = map(int, input().split())

dict = {}
for _ in range(l):
    stu = input().rstrip()

    if stu not in dict:
        dict.setdefault(stu,0)
    else:
        dict.pop(stu)
        dict.setdefault(stu,0)

cnt = 0
for i in dict.keys():
    print(i)
    cnt += 1
    if cnt == k:
        break


# 시간초과 이거 해쉬인듯?
# # q = deque()
# q = []
# for _ in range(l):
#     stu = int(input())
#     if stu not in q:
#         q.append(stu)        
#     else:
#         qidx = q.index(stu)
#         q.pop(qidx)
#         q.append(stu)
# for i in range(k):
#     print(q[i])