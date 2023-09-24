n = int(input())
five_cnt = 0
three_cnt = 0
flag = True
while n >= 3 and flag:
    if n % 5 == 0:
        five_cnt += n / 5
        break
    elif n % 5 != 0:
        for i in range(1,6):
            three_cnt += 1
            if (n - 3*i) < 0:
                n = 0
                break
            if (n - 3*i) % 5 == 0:
                five_cnt += (n-3*i) / 5
                flag = False
                break
        else:
            if n % 3 == 0:
                three_cnt += n/3
                break
        if flag:
            n -= 3
            three_cnt += 1
if n < 3:
    print(-1)
else:
    print(int(three_cnt + five_cnt))