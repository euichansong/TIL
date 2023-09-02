import sys
from collections import deque
q = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    order = list(sys.stdin.readline().split())
    # push_front
    if order[0] == 'push_back':
        a = order[1]
        b = ''.join(a)
        q.append(int(b))
    # push_back
    elif order[0] == 'push_front':
        a = order[1]
        b = ''.join(a)
        q.appendleft(int(b))
    # pop_fr
    elif order[0] == 'pop_front':
        if q:
            a = q.popleft()
            print(a)
        else:
            print(-1)
    # pop_ba
    elif order[0] == 'pop_back':
        if q:
            a = q.pop()
            print(a)
        else:
            print(-1)
    # size
    elif order[0] == 'size':
        print(len(q))
    # empty
    elif order[0] == 'empty':
        if not list(q):
            print(1)
        else:
            print(0)
    # front
    elif order[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    # back
    elif order[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)