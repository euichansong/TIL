s,d,i,l,n = map(int, input().split())
avg = (s+d+i+l) / 4
cnt = 0

while True:
    if avg >= n:
        break
    else:
        avg += 0.25
        cnt += 1
print(cnt)