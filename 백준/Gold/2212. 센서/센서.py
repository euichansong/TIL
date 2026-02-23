"""
2 초	128 MB

센서는 모두 통신해야 한다 2개 이상도 가능
센서 좌표 같을수도 있다

예제 1번은 1 3 6 6 7 9

2, 7 에 놓으면 1 1 1 1 2 최소값 5?? 6인데

그룹으로 묶는다? 예외처리 나올듯 k가 2일때 123 8 20 30

센서간의 거리차이를 만들어서 반으로 줄인다? 
>> 최대 k개의 집중국이니까 k보다 적게 만들수도 있다?
>> 한번 반갈하고 다시 거리차이 리스트에 집어넣어서 다시 소트 하고 반복?
>> 1 2 10 20 이면 k1일때 15

아 [1,3] [6,9] 범위 이렇게 최소값이 5인거구나

k가 더 많을때는? 최대 k개 설치니까 상관없나
"""
import sys
input = sys.stdin.readline

# 센서의 갯수
n = int(input())
# 집중국의 갯수
k = int(input())
# 센서의 좌표
sensor = list(map(int, input().split()))
sensor.sort()

gap = [0] * (n-1)

for i in range(n-1):
    gap[i] = sensor[i+1] - sensor[i]

gap.sort(reverse=True)
# print(gap)
ans = sum(gap[k-1:])

print(ans)
