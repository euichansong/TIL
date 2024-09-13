def solution(n):
    answer = 0
    bin_n = str(bin(n)[2:])
    one_cnt = bin_n.count('1')
    for i in range(n+1,1000001):
        bin_i = str(bin(i)[2:])
        i_one = bin_i.count('1')
        if one_cnt == i_one:
            answer = i
            break
    return answer