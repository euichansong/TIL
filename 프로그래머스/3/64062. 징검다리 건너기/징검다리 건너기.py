# """
# k칸 이상 넘을수 없다
# 다음칸이 연결되어있으면 가까운 디딤돌로 뛸수 있다

# """
# def solution(stones, k):
#     answer = 0
#     lens = len(stones)   
#     # 최소값 구해서 빼고 시작
#     mins = min(stones)
#     for i in range(lens):
#         stones[i] -= mins
#     answer += mins

#     idx = 0
#     zero_idx = 0
    
#     while True:
#         if zero_idx == k:
#             break
#         # 1인경우 무한루프
#         if lens == 1:
#             return answer
#         if idx == lens-1:
#             idx = 0
#             answer += 1
#         else:
#             if stones[idx] == 0:
#                 idx += 1
#                 zero_idx += 1
#                 if zero_idx == k:
#                     return answer
#             else:
#                 stones[idx] -= 1
#                 idx += 1
#                 zero_idx = 0
#     return answer
def solution(stones, k):
    left, right = 1, max(stones)  # 가능한 최소값과 최대값을 탐색 범위로 설정
    
    while left <= right:
        mid = (left + right) // 2  # 중간값 설정
        cnt = 0  # 0이 연속된 횟수
        
        for stone in stones:
            if stone - mid <= 0:  # 이 디딤돌을 밟을 수 없으면
                cnt += 1  # 0이 연속됨
            else:
                cnt = 0  # 다시 0이 아닌 돌을 만남
            
            if cnt >= k:  # 연속된 0의 길이가 k 이상이면
                break
        
        if cnt >= k:  # 더 많은 사람은 건널 수 없음
            right = mid - 1
        else:  # 더 많은 사람이 건널 수 있음
            left = mid + 1
    
    return left