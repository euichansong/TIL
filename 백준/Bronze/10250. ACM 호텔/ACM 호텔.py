t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    cnt = 0
    flag = True
    for i in range(1,w+1):
        for j in range(1,h+1):
            cnt += 1
            if cnt == n:
                # print(j,i)
                flag = False
                break
        if not flag:
            break

    print(j*100+i)