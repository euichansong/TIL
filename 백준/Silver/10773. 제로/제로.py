import sys
from collections import deque
q = deque()
k = int(sys.stdin.readline())

for i in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        q.pop()
    else:
        q.append(num)
print(sum(q))