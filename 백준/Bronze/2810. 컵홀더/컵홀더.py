n = int(input())
s = list(input())
cnt = 1  

i = 0
while i < n:
    if s[i] == 'S':
        cnt += 1
    elif s[i] == 'L':
        cnt += 1  
        i += 1   
    i += 1

# sss인 경우
print(min(cnt, n))
