def solution(arr):
    answer = 0
    max_arr = max(arr)
    for i in range(1,1000000):
        temp = max_arr * i
        cnt = 0
        for j in arr:
            if (temp % j) != 0:
                continue
            else:
                cnt += 1
        if cnt == len(arr):
            answer = temp
            break
        
    return answer