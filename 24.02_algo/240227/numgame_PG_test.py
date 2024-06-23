from collections import deque


def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    # B = deque(B)
    # print(A,B)

    a_idx = 0
    # b 하나 골라서
    for b_num in B:
        # a 값 인덱스 1씩 더하면서 b 값보다 크지 않을때까지
        while a_idx < len(B) and A[a_idx] < b_num:
            answer += 1
            a_idx += 1
            break

    return answer
a = [5,1,3,7]
b = [2,2,6,8]
print(solution(a,b))