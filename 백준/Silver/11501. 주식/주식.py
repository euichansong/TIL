from collections import deque
import sys,copy
# sys.stdin = open("11501.txt")
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    sell = 0
    ans = 0
    for i in range(n-1,-1,-1):
        if price[i] < sell:
            ans += sell-price[i]
        else:
            sell = price[i]
    print(ans)