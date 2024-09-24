# """
# 00 01 
# 10 11
#       02
#       12
# 20 21 22
# 인덱스 같으면 그 숫자 다르면 큰숫자
# """
# def solution(n, left, right):
#     matrix = [[n] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 matrix[i][j] = j+1
#             elif i > j:
#                 matrix[i][j] = i+1
#             else:
#                 matrix[i][j] = j+1
#     change_one = []   
#     for i in matrix:
#         change_one += i
#     answer = change_one[left:right+1]       
#     return answer
def solution(n, left, right):
    answer = []
    
    for k in range(left, right+1):
        i = k//n 
        j = k%n 
        answer.append(max(i, j)+1)
    
    return answer