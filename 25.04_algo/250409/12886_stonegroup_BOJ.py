"""
크기 다른 2개 그룹 고른다

x y

x+x, y-x

크기 차이 많이 나는걸로 바꿔야 하나
10 35 15
20 25

1 1 7

2 0 7

1 2 6
1 6
2 5
2 2 5
2 5
4


25 15 20
30 10
20 20
15 35
30 20

3배수 아니면 무조건 0

2 초	512 MB
이게 그래프?
나가는 과정 찾는거니까?
"""
import sys
from collections import deque
a,b,c = map(int,input().split())

total = a + b + c

if total % 3 != 0:
    print(0)
else:
    visited = set()
    q = deque()

    start = tuple(sorted([a, b, c]))
    q.append(start)
    visited.add(start)

    while q:
        x, y, z = q.popleft()
        if x == y == z:
            print(1)
            break

        for i, j in ((x, y), (y, z), (x, z)):
            if i != j:
                s = min(i, j)
                l = max(i, j)
                ni = s + s
                nj = l - s
                nk = total - i - j
                new_state = tuple(sorted([ni, nj, nk]))
                if new_state not in visited:
                    visited.add(new_state)
                    q.append(new_state)
    else:
        print(0)




