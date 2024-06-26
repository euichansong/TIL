from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nlist = list(map(int, input().split()))
# 정렬
nlist.sort()
nlist = deque(nlist)

answer = 0
# 길이가 1보다 클때까지
while len(nlist) > 1:
    # 가장 작은값 큰값 더해서 m보다 크면 
    if nlist[0] + nlist[-1] >= m:
        # 작은값 빼고
        nlist.popleft()
        # 큰값 뺀다
        nlist.pop()
        answer += 1
    else:
        # 아니면 가장 작은값 빼고 다시
        nlist.popleft()
print(answer)