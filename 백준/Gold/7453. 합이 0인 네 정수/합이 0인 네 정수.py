"""
배열 정렬후 합 기준 중간값 비교해서 값 찾기
합이 - 인 경우 뒤 배열 맥스값 합쳐도 안되면 pass
12초 n log n ?
a,b 2개 잡고 c d 맥스값 보다 작으면 패스 
a 돌면서 bcd 맥스값 보다 작으면 패스
abc 돌면서 d 맥스 보다 작으면 패스

합이 0보다 큰 경우 작은값부터
    0보다 작은경우 큰값부터

이제 어떻게 인덱스를 선택하지? 

4개를 2개로 줄이면 된다
> a,b c,d
"""
import sys
input = sys.stdin.readline
n = int(input())
al,bl,cl,dl = [],[],[],[]

for i in range(n):
    a,b,c,d = map(int, input().split())
    al.append(a)
    bl.append(b)
    cl.append(c)
    dl.append(d)
abl = []
cdl = []
for a in al:
    for b in bl:
        abl.append(a+b)
for c in cl:
    for d in dl:
        cdl.append(c+d)
abl.sort()
cdl.sort()
right = len(abl)-1
left = 0
ans = 0
sa = 0

# ab는 오른쪽 cd는 왼쪽부터 
while 0 <= right and left < len(abl):
    sa = abl[left] + cdl[right]
    if sa < 0:
        left += 1
    elif sa > 0:
        right -= 1
    else:
        # 겹친 숫자 찾기
        l = 1
        r = 1
        for q in range(left+1,len(abl)):
            if abl[left] == abl[q]:
                l += 1
            else:
                break
        for q in range(right-1,-1,-1):
            if cdl[right] == cdl[q]:
                r += 1
            else:
                break
        left += l
        right -= r
        # lr 로 짤수있는 조합
        ans += l*r

print(ans)
