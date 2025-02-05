"""
1 초	128 MB
적어도 k개 먹어야 
선영이는 남는거만

구매는 1개만
막대는 정사각형 d 개 막대면 나눌때 d/2개

6개 만들려면

k에서 choco  //2 빼고 남은거 
"""

k = int(input())
choco = 1
while choco < k:
    choco *=2
ans1 = choco
ans2 = 0
cho = choco
while k > 0:
    # k보다 작고 가장 가까운 2의 제곱수
    if cho > k:
        cho //= 2
        ans2 += 1
    else:
        k -= cho
print(ans1,ans2)
    
