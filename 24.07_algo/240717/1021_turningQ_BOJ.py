from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
qlist = list(map(int, input().split()))

"""
1. pop 하는건 연산 갯수 안들어간다
2. 순서대로 q에 넣고 pop append 하고 카운트한다
"""
q = deque()
for i in range(n):
    q.append(i+1)

answer = 0
halfidx = n // 2

for i in qlist:
    while True:
        if i == q[0]:
            q.popleft()
            break
        else:
            halfidx = len(q)//2
            # 현재 숫자의 위치가 중간보다 작으면
            if q.index(i) <= halfidx:
                # 맨 앞 숫자 빼서
                t = q.popleft()
                # 뒤에 넣고
                q.append(t)
                answer += 1
            # 크면 앞에 더한다
            else:
                # 맨 뒤 숫자 빼서
                t = q.pop()
                # 앞에 넣고
                q.appendleft(t)
                answer += 1
print(answer)