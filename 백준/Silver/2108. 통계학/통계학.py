import copy,sys
input = sys.stdin.readline
n = int(input())
nl = [int(input()) for _ in range(n)]
a = int(round(sum(nl) / n,0))
b = nl.copy()
b.sort()
bb = b[n//2]

dict = {} # {1: 1}
for i in range(n):
    if b[i] not in dict:
        dict[b[i]] = 1
    else:
        dict[b[i]] += 1

mx = max(dict.values())
mxl = []
for i in dict:
    if mx == dict[i]:
        mxl.append(i)
d = max(nl) - min(nl)

print(a)
print(bb)

if len(mxl) > 1:
    # mxl.sort()
    print(mxl[1])
else:
    print(mxl[0])

print(d)