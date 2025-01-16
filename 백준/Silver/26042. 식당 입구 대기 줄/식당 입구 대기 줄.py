"""
0.1 초	512 MB
"""
import sys
input = sys.stdin.readline
n = int(input())
q = []
m = 0
ans = 0
for _ in range(n):
    c = input().split()
    if c[0] == '1':
        wait = int(c[1])
        q.append(wait)
    elif c[0] == '2':
        if q:
            q.pop(0)
    if len(q) > m:
        m = len(q)
        ans = q[-1]
    elif len(q) == m:
        if q[-1] < ans:
            ans = q[-1]
print(m, ans)
