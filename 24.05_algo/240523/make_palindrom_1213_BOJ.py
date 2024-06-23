"""
길이 짝수인 경우 다 짝수개
길이 홀수인 경우 1개만 홀수 나머진 다 짝수
딕셔너리?
DCBAD

홀수 2개 이상이면 끝
나머지는 갯수의 반만 더한다
그리고 총 갯수에 더하고 홀수 문자 넣고 뒤집은값 [::-1] 더한다
"""
a = list(input())
lena = len(a)
dict = {}

for i in a:
    if i not in dict:
        dict.setdefault(i,1)

    else:
        dict[i] += 1
# print(dict)
# 오름차순 알파벳
low = sorted(dict.keys())
# print(low)
# 카운트로 홀수 2개 이상이면 실패
cnt = 0
od = ''

for i in low:
    if dict[i] % 2 == 1:
        cnt += 1
        od += i
    if cnt > 1:
        print("I'm Sorry Hansoo")
        exit()
# print(od)
answer = ''
for j in low:
    answer += (dict[j]//2 * j)


if od:
    answer = answer + od + answer[::-1]
else:
    answer = answer + answer[::-1]

print(answer)