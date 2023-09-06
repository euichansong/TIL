n, m = map(int, input().split())
# 듣도 못한 사람
knowlist = []
# 보도 못한 사람
unknownlist = []
for i in range(n):
    know = input()
    knowlist.append(know)
for i in range(m):
    unknown = input()
    unknownlist.append(unknown)
# print(knowlist)
# print(unknownlist)
# 교집합
res = list(set(set(knowlist) & set(unknownlist)))
# 오름차순
res.sort()
# 출력
print(len(res))
for i in range(len(res)):
    print(res[i])