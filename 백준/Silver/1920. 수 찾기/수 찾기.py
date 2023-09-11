n = int(input())
num = list(map(int, input().split()))
num = set(num)
m = int(input())
mlist = list(map(int, input().split()))
for i in mlist:
    if i in num:
        print(1)
    else:
        print(0)