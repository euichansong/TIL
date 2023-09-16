import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s_dict = {}
for i in range(n):
    s_dict[input().rstrip()] = 0
cnt = 0
for i in range(m):
    check = input().rstrip()
    if check in s_dict:
        cnt += 1
print(cnt)