def cal(num_idx, res):
    global maxres
    global minres
    if num_idx == n-1:
        maxres = max(maxres, res)
        minres = min(minres, res)
        return
    for op in range(4):
        if oper_list[op] > 0:
            oper_list[op] -= 1
            if op == 0:
                new_res = res + numlist[num_idx + 1]
            elif op == 1:
                new_res = res - numlist[num_idx + 1]
            elif op == 2:
                new_res = res * numlist[num_idx + 1]
            elif op == 3:
                new_res = res / numlist[num_idx + 1]
                new_res = int(new_res)
            cal(num_idx+1, new_res)
            oper_list[op] += 1


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    oper_list = list(map(int, input().split()))
    numlist = list(map(int, input().split()))
    maxres = -100000000
    minres = 100000000
    cal(0, numlist[0])
    # print(maxres)
    # print(minres)
    print(f'#{tc} {maxres-minres}')