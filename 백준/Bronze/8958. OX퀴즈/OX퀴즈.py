t = int(input())
for _ in range(t):
    oxlist = list(input())
    res = []
    cnt = 0
    for i in oxlist:

        if i =='O':
            cnt += 1
        else:
            cnt = 0
        res.append(cnt)
    print(sum(res))