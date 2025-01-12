import sys
from collections import deque
input = sys.stdin.readline
"""
큐랑 비교, 리스트랑 비교

5
5 2 4 1 3
"""
n = int(input())
stu = list(map(int,input().split()))

def pro(stu):
    stu = deque(stu)
    w = deque()
    now = 0
    while stu or w:
        # print(w,now)
        
        if w and w[-1] == now + 1:
            w.pop()
            now += 1
        elif stu:
            p = stu.popleft()
            w.append(p)
        else:
            return now
        
    return now

ans = pro(stu)
if ans == n:
    print("Nice")
else:
    print("Sad")

# def pro(stu):
#     stu = deque(stu)
#     w = deque()
#     now = 0
#     p = stu.popleft()
#     w.append(p)
#     while w:
#         if now+1 == w[-1]:
#             w.pop()
#             now += 1
#         if stu:
#             p = stu.popleft()
#             w.append(p)
#             if now+1 == w[-1]:
#                 w.pop()
#                 now += 1
#         # 줄 서있는거 없고 스택 마지막이 다르면
#         if not stu:
#             if w and w[-1] != now+1:
#                 return now
            
#     return now


