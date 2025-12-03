"""
1.5 초	512 MB

10개 키워드 글 작성
글 쓰고 메모장에서 지워짐
글에 있는 키워드 갯수 10개까지

메모장에 키워드 없으면 글써도 추가 안된다
1 ≤ N ≤ 200000

딕셔너리로 키값 밸류값 1 넣고 있으면 -1 해준다 개수가 0이면 체크 안함
>> 키워드가 모두 다르기 때문에 괜찮을듯
>>>> 시간초과
>>>> 아예 팝을 해버린다
"""
import sys
input = sys.stdin.readline
# 키워드갯수 n, 글의 갯수 m
n,m = map(int, input().rstrip().split())
dict = {}
for _ in range(n):
    key = input().rstrip()
    dict.setdefault(key,1)
    
for _ in range(m):
    using = list(input().rstrip().split(','))
    for i in range(len(using)):
        if using[i] in dict:
            dict.pop(using[i])
    #print(dict)
    ans = len(dict)
    print(ans)

# 시간초과
# for _ in range(m):
#     using = list(input().split(','))
#     for i in range(len(using)):
#         if using[i] in dict and dict[using[i]] != 0:
#             dict[using[i]] -= 1
#     ans = sum(dict.values())
#     print(ans)


