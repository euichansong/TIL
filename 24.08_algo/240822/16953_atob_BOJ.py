"""
3,5,7,9 는 만들수 없다
visited 를 써서 푸니까 메모리 초과 발생
>> 횟수를 q에 같이 넣고 돌리자
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

"""
from collections import deque
a,b = map(int, input().split())
def bfs(start,end):
    visited = [0] * b
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        t = q.popleft()
        if t == end:
            return visited[end]
        for i in [10*t + 1, t*2]:
            if i <= b:
                q.append(i)
                visited[i] = visited[t] + 1
    return -1
answer = bfs(a,b)
# print(answer)
# if answer == 0:
#     print(-1)
# else:
print(answer)

"""