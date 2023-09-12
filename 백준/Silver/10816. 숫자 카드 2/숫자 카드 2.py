n = int(input())
num = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))
cntlist = {}
for i in num:
    if i in cntlist:
        cntlist[i] += 1
    else:
        cntlist[i] = 1

for i in mlist:
    if i in cntlist:
        print(cntlist[i], end = ' ')
    else:
        print(0, end = ' ')