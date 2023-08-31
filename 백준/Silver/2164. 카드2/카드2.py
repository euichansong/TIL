from collections import deque

n = int(input())
nlist = [i for i in range(1,n+1)]
deq = deque(nlist)

while len(deq) >= 2:
    deq.popleft()
    b = deq.popleft()
    deq.append(b)

print(*deq)
