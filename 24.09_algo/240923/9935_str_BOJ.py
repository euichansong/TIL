"""
폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.
=> 폭문의 시작으로 알수 있다
시간초과 11퍼
"""
# import sys
# input = sys.stdin.readline
# m = input().rstrip()
# e = input().rstrip()
# le = len(e)
# idx = 0
# while True:
#     if idx >= len(m):
#         break
#     if m[idx] == e[0]:
#         if m[idx:idx+le] == e:
#             fe = m[0:idx]
#             ee = m[idx+le:]
#             m = fe + ee
#             if idx-le < 0:
#                 idx = 0
#             else:
#                 idx -= le
#         else:
#             idx+= 1
#     else:
#         idx += 1
# if len(m) == 0:
#     print("FRULA")
# else:
#     print(m)
import sys
input = sys.stdin.readline
m = list(input().rstrip())
e = list(input().rstrip())
le = len(e)
s = []
for i in m:
    s.append(i)
    aa = s[len(s)-le:len(s)]
    if aa == e:
        for _ in range(le):
            s.pop()

if s:
    print(*s,sep='')
else:
    print("FRULA")
