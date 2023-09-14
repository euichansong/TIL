n1, n2 = map(int,input().split())

cnt = 2
n1list = [1,n1]
while 0 < n1 and n1 > cnt:
    if float(n1 // cnt) == float(n1/cnt):

        n1list.append(cnt)
        cnt += 1
    else:
        cnt += 1
cnt2 = 2
n2list = [1,n2]
while 0 < n2 and n2 > cnt2:
    if float(n2 // cnt2) == float(n2/cnt2):

        n2list.append(cnt2)
        cnt2 += 1
    else:
        cnt2 += 1
# print(n1list,n2list)
print(max(list(set(n1list) & set(n2list))))
# 최대공약수는 공약수중 가장 큰 수
maxgong = max(list(set(n1list) & set(n2list)))
# 최소공배수는 최대공약수 * (각 숫자 // 최대공약수)
print(n1* n2 // maxgong)