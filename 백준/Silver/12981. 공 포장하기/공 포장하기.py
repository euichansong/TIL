r, g, b = map(int, input().split())
"""
박스안에는 공이 1 2 3 개 들어갈수 있다 
박스안에 들어가는 공의 색은 모두 다르거나 모두 같아야한다
"""

"""
1. 우선 가능한 만큼 모두 다른색으로 3개를 박스에 넣는다. (따라서 정렬 후, 가장 낮은 값을 나머지 2개에서 빼줬다.)
2. 이제 3개씩 넣을 수 있는 방법은 모두 같은 색으로 3개를 넣는 방법 뿐이다. 따라서 남은 2개의 색상은 각각 3개씩 가능한 만큼 넣어준다.
3. '2'에서 남은 공운 1개 아니면 2개일 것이다(3개씩 넣었으므로). 이 때 가능한 경우는 다음과 같다.
3.1 둘다 남은게 0개인 경우 -> 모두 3개씩 들어간 경우이다. 1~2에서 구한것만 출력해주면 된다.
3.2 한쪽이 남은게 0인 경우 -> 나머지 하나를 상자 하나에 넣어주면 된다. 1~2에서 구한 값 + 1을 출력해주면 된다.
3.3 둘 다 1개씩 남은 경우 -> 이 경우 2개짜리 상자 하나만 있으면 된다. 마찬가지로 +1을 출력해준다.
3.4 이제 남은 경우는 둘 다 2개인 경우와 둘이 1개와 2개가 남은 경우 -> 이 경우엔 +2를 해줘야 한다.
"""
#  red 1 green 2  blue 3
cnt = min(r, g, b)
r -= cnt
g -= cnt
b -= cnt
cnt += r//3 + g //3 + b // 3
r %= 3
g %= 3
b %= 3
# print(r,g,b)
# print(cnt)
if r == 0 and g == 0 and b != 0:
    cnt += 1
elif r == 0 and g != 0 and b == 0:
    cnt += 1
elif r != 0 and g == 0 and b == 0:
    cnt += 1


elif r == 1 and g == 1 and b == 0:
    cnt += 1
elif r == 1 and g == 0 and b == 1:
    cnt += 1
elif r == 0 and g == 1 and b == 1:
    cnt += 1

elif r == 2 and g == 1 and b == 0:
    cnt += 2
elif r == 1 and g == 2 and b == 0:
    cnt += 2
elif r == 2 and g == 0 and b == 1:
    cnt += 2
elif r == 1 and g == 0 and b == 2:
    cnt += 2
elif r == 0 and g == 1 and b == 2:
    cnt += 2
elif r == 0 and g == 2 and b == 1:
    cnt += 2

elif r == 2 and g == 2 and b == 0:
    cnt += 2
elif r == 2 and g == 0 and b == 2:
    cnt += 2
elif r == 0 and g == 2 and b == 2:
    cnt += 2

print(cnt)