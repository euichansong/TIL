import sys
input = sys.stdin.readline
# 출력시 끝에 '\n' 나와서 strip 사용
num = input().strip()
# 카운트
cnt = 0
# num의 길이가 1 보다 클 때 까지 ( 합이 한자리 수 일때 까지)
while len(num) > 1:
    # sum을 쓰기 위해 int형으로 변환
    total = sum(map(int, num))
    # while의 조건인 len 을 쓰기 위해 다시 문자열로 변환
    num = str(total)
    # 카운트 증가
    cnt += 1
print(cnt)
if int(num) % 3 == 0:
    print('YES')
else:
    print('NO')

# 시간 초과
# num = int(input())
# cnt = 0
# while num > 9:
#     list_num = []
#     while num > 9:
#         a = num % 10
#         num //= 10
#         list_num.append(a)
#     list_num.append(num)
#     sum_num = sum(list_num)
#     num = sum_num
#     cnt += 1
# print(cnt)
# if num % 3 == 0:
#     print('YES')
# else:
#     print('NO')