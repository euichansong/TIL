import sys
input = sys.stdin.readline
n = int(input())
nl = [0]+[int(input()) for _ in range(n)]
nl.sort()
ans = 0
for i in range(1,n+1):
    ans += abs(nl[i]-i)
print(ans)
