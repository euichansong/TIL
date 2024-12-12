import sys
input = sys.stdin.readline
n = int(input())
minus = list(map(int, input().split()))
plus = list(map(int, input().split()))
"""
백트로 해볼까 n 20밖에 안되는데
"""
# visited = [0] * n
ans = 0
def backt(idx,hp,total):
    global ans
    if hp > 0:
        ans = max(ans,total)
    # n-1로 하면 답이 안맞네
    if idx == n:
        return
    # 1번 인사 안하는 경우
    backt(idx+1,hp,total)
    # 체력 0보다 클수 있는 경우
    if hp - minus[idx] > 0:
        backt(idx+1,hp-minus[idx],total + plus[idx])

backt(0,100,0)
print(ans)
