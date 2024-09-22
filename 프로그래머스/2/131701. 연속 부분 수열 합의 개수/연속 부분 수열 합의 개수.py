# 시간 초과 
# def solution(elements):
#     e = len(elements)
#     answer = 0
#     max_len = 1
#     l = []
#     while max_len <= e:
#         for i in range(e):
#             sum = 0
#             for j in range(i,i+max_len):
#                 if j <= e-1:
#                     sum += elements[j]
#                 else:
#                     j = j % e
#                     sum += elements[j]
#             l.append(sum)
#         max_len += 1
#     l = list(set(l))
#     answer = len(l)
#     return answer
def solution(elements):
    e = len(elements)
    elements = elements * 2  # 원형 배열을 처리하기 위해 두 배로 확장
    unique_sums = set()

    # max_len에 대해 부분합 계산
    for max_len in range(1, e + 1):
        for i in range(e):
            unique_sums.add(sum(elements[i:i + max_len]))
    
    return len(unique_sums)