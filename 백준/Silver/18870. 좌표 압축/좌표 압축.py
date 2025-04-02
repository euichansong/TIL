"""
2 초	512 MB
2 > -10,-9
4 2-9-10
-10 0
자기보다 작은 갯수 구하기

겹치는건? set 
"""
n = int(input())
nlist = list(map(int, input().split()))
set_list = list(set(nlist))
sort_list = sorted(set_list)
dict = {}
for i in range(len(sort_list)):
    dict[sort_list[i]] = i
for i in nlist:
    print(dict[i],end=' ')