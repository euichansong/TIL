import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1 << n):
    res = []
    for j in range(n):
        if i & (1 << j):
            res.append(arr[j])
    if res:
        result = sum(res)
        if result == s:
            cnt += 1    
print(cnt)
