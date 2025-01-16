"""
1 초	1024 MB
"""
n = int(input())
tech = list(input())
rt = 0
kt = 0
ans = 0
for i in tech:
    if i == 'L':
        rt +=1
    elif i == 'R':
        if rt>0:
            ans += 1
            rt -=1
        else:
            break
    elif i == 'S':
        kt +=1
    elif i == 'K':
        if kt>0:
            ans += 1
            kt -=1
        else:
            break
    else:
        ans += 1
print(ans)

