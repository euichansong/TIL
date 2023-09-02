import sys
from collections import deque
q = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    order = list(sys.stdin.readline())
    # push
    if order[1] == 'u':
        a = order[5:]
        b = ''.join(a)
        q.append(int(b))
    # pop
    if order[1] == 'o':
        if q:
            a = q.popleft()
            print(a)
        else:
            print(-1)
    # size
    if order[1] == 'i':
        print(len(q))
    # empty
    if order[1] == 'm':
        if not list(q):
            print(1)
        else:
            print(0)
    # front
    if order[1] == 'r':
        if q:
            print(q[0])
        else:
            print(-1)
    # back
    if order[1] == 'a':
        if q:
            print(q[-1])
        else:
            print(-1)
