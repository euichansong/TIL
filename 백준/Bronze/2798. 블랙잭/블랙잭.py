n, m = map(int, input().split())
card = list(map(int, input().split()))
length = len(card)
cnt = 0
res = []
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            res.append(card[i]+card[j]+card[k])
# print(res)
min = 300000
for i in res:
    min_abs = m-i
    if min_abs >= 0 and min > min_abs:
        min = min_abs
print(m-min)
