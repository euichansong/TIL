"""

"""
import sys

input = sys.stdin.readline

n = int(input())
coding = list(map(int, input().split()))

coding.sort()

ans = 1e9
for i in range(n):
    mini = coding[i] + coding[-(i+1)]
    # print(mini)
    ans = min(mini,ans)
print(ans)