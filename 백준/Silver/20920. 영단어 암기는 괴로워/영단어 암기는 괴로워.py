"""
1 초 (추가 시간 없음)	1024 MB
빈도수
길이
사전
"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

dic = {}
for _ in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    if word not in dic:
        dic.setdefault(word,1)
    else:
        dic[word] += 1

sort_dic = sorted(dic.items(), key= lambda x: (-x[1],-len(x[0]),x[0]))
for i in range(len(sort_dic)):
    print(sort_dic[i][0])


