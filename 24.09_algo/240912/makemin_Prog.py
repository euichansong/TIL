"""
가장 큰수 * 가장 작은수?
1000*1000이니까 백트레킹, 재귀 x

"""
def solution(A,B):
    answer = 0
    a = sorted(A)
    b = sorted(B,reverse=True)
    print(a,b)
    # for i in range(len(a)):
    #     answer += a[i]*b[i]

    return answer
A = [1, 4, 2]
B = [5, 4, 4]
solution(A,B)