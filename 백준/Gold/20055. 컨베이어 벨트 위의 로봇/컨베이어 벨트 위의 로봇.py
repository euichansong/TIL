import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
belt = list(map(int,input().split()))
move = [0] * n
move = deque(move)
belt = deque(belt)
answer = 0
while True:
    answer += 1
    # 회전
    move.rotate(1)
    belt.rotate(1)
    # 내림
    move[n-1] = 0
    # 내리는거 부터 확인후 내구도 깎기
    for i in range(n-2,-1,-1):
        # 다음 칸 내구도 1 이상, 다음 벨트에 있는 로봇 X 지금 로봇 O
        if belt[i+1] >= 1 and move[i+1] == 0 and move[i] == 1:
            move[i+1] = 1
            move[i] = 0
            belt[i+1] -= 1
    # 내림
    move[n - 1] = 0

    # 올림
    if belt[0] != 0:
        move[0] = 1
        belt[0] -= 1
    cnt = 0
    for i in range(len(belt)):
        if belt[i] == 0:
            cnt += 1
    if cnt >= k:
        break
print(answer)