""" 해설 확인 + 내가 이해한것 
연속적인 숫자를 이어 붙임

>>> 주어진 숫자에서 0부터 하나씩 올라가면서 주어진 숫자의 첫번째값과 비교 
>>> 같으면 지우고 다음숫자 갱신 

234092 기준

0,1 안되고
2에 234092 의 첫번째 2와 일치 > num을 34092로 바꾸고 다음숫자
다음숫자 3일때 34092의 첫번째 3과 일치  > num을 4092로 바꾸고 다음숫자
다음숫자 4일때 4092의 첫번째 4과 일치  > num을 092로 바꾸고 다음숫자
...
10일때 092의 첫번째 0 > 제거 92로 바뀜
19일때 9 제거
20일때 2 제거 

"""

num = list(input())

def number(num):
    n = 0
    while True:
        n += 1
        cnt = str(n)
        while len(cnt)>0 and len(num)>0:
            if num[0] == cnt[0]:
                num = num[1:]
            cnt=cnt[1:]
            if len(num) == 0:
                print(n)
                return

number(num)


""" 내가 생각했던 풀이 결국 최소값을 구할수 없음
2 초	128 MB

9까지 1은 1개
99까지 1은 20개
999까지 1은 300개
9999 1 4000
99999 1 50000

for i in range(100000):
    i = list(str(i))
    ans += i.count('1')
        
print(ans)

> 빈도수 가장 높아야 3000

숫자 카운트 해서 가장 빈도수 높은값 
>  4자리수 안넘으니까 그냥 다 카운트 
"""
# num = list(input())
# dict = {1:0, 2:0, 3:0,4:0,5:0,6:0,7:0,8:0,9:0,0:0}
# for i in num:
#     dict[int(i)] += 1
# ds = sorted(dict.items(), key=lambda x: x[1], reverse=True)
# print(ds)
