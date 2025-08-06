"""
제한
1 초	256 MB

풀이 생각
처음기준 그 높이보다 크거나 같을때 까지 계산
기준으로 놓고 고일때까지 기준에서 빼기 
>>>>> xxxx 왼쪽만 높다고 생각해서 틀림

+ 양끝은 생각할 필요 없다

자기 기준 양옆에 찾아서 최소값? 이거 되나 
"""
h,w = map(int, input().split())
height = list(map(int, input().split()))

ans = 0
for i in range(1,w-1):
    l = height[:i]
    r = height[i+1:]
    # 가장 큰값들중에 가장 작은값
    mi = min(max(l),max(r))
    # 0이 아니고 벽이 더 큰 경우 
    if mi != 0 and mi > height[i]:
        ans += (mi - height[i])
print(ans)