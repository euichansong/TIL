"""
3,5,7,9 는 만들수 없다
"""

from collections import deque
a,b = map(int, input().split())
def bfs(start,end):

    q = deque()
    q.append([start,1])

    while q:
        n,t = q.popleft()
        if n == end:
            print(t)
            break
        for i in [10*n + 1, n*2]:
            if i <= b:
                q.append([i,t+1])

    else:
        print(-1)
bfs(a,b)

