"""
완탐?
b 하나 골라서 a 요소 보다 작은 값 나올때 까지
"""
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()

    # for i in range(len(B)):
    #     for j in range(i, len(A)):
    #         if A[j] < B[i]:
    #             answer += 1
    #             break
    a_idx = 0
    for b_num in B:
        while a_idx < len(B) and A[a_idx] < b_num:
            answer += 1
            a_idx += 1
            break
            
                
    return answer