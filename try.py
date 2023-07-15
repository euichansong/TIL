T = int(input())
for test_case in range(1, T + 1):
    tc = int(input())
    score = list(map(int, input().split()))
    count = [0] * 101
    max = 0
    max_i = 0
    for i in range(1000):
        count[score[i]] += 1
    for i in range(101):
        if count[i] >= max:
            max = count[i]
            max_i = i
    print('#{} {}'.format(test_case, max_i))