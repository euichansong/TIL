# m = int(input())
# s = []
# for _ in range(m):
#     arr = list(input().split())
#     oper = arr[0]
#     if len(arr) == 2:
#         num = arr[1]
#         num = int(num)
#     if oper == 'add':
#         if num in s:
#             pass
#         else:
#             s.append(num)
#     elif oper == 'remove':
#         if num in s:
#             s.remove(num)
#     elif oper == 'check':
#         if num in s:
#             print(1)
#         else:
#             print(0)
#     elif oper == 'toggle':
#         if num in s:
#             s.remove(num)
#         else:
#             s.append(num)
#     elif oper == 'all':
#         s = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#     elif oper == 'empty':
#         s = []

# ========================
import sys
input = sys.stdin.readline
m = int(input())
s = set()
for _ in range(m):
    arr = list(input().split())
    oper = arr[0]
    if len(arr) == 2:
        num = arr[1]
        num = int(num)
    if oper == 'add':
        if not num in s:
            s.add(num)
    elif oper == 'remove':
        if num in s:
            s.remove(num)
    elif oper == 'check':
        if num in s:
            print(1)
        else:
            print(0)
    elif oper == 'toggle':
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif oper == 'all':
        s = set([i for i in range(1,21)])
    elif oper == 'empty':
        s = set()