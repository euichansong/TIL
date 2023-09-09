a = int(input())
b = int(input())
c = int(input())
gob = a*b*c
cnt = [0] * 10
# print(gob)
while gob > 0:
    cnt[gob % 10] += 1
    gob //= 10
for i in cnt:
    print(i)
# print(cnt)