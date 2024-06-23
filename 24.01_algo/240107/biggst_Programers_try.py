def solution(numbers):
    str_num = []
    for i in numbers:
        i = str(i)
        str_num.append(i)
    N = len(str_num)
    answer_list = []
    permition(str_num, N, 0)
    answer = ''
    return answer


def permition(str_num, N, idx):
    if idx == N:
        num = ''
        for i in str_num:
            num += i
        print(num)

    else:
        for i in range(idx, N):
            str_num[idx], str_num[i] = str_num[i], str_num[idx]
            permition(str_num, N, idx + 1)
            str_num[i], str_num[idx] = str_num[idx], str_num[i]

