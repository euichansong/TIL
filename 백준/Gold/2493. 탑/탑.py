import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
topl = list(map(int, input().split()))
answer = [0] * n
stack = []
for i in range(n):
    # 나보다 낮은 탑(인덱스)의 높이는 모두 pop
    while stack and topl[stack[-1]] < topl[i]:
        stack.pop()
    # 남아 있으면 그 인덱스가 나의 수신탑
    if stack:
        # +1 해서 ‘번호’로 변환
        answer[i] = stack[-1] + 1    
    # 내 인덱스도 다음 탑들이 볼 수 있도록 push
    stack.append(i)

print(*answer)