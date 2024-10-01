def solution(topping):
    answer = 0
    left_set = set()
    right_set = set()
    
    # 왼쪽에서 순차적으로 등장하는 토핑 종류 수 기록
    left_counts = []
    for t in topping:
        left_set.add(t)
        left_counts.append(len(left_set))
    
    # 오른쪽에서 순차적으로 등장하는 토핑 종류 수 기록
    right_counts = [0] * len(topping)
    for i in range(len(topping) - 1, -1, -1):
        right_set.add(topping[i])
        right_counts[i] = len(right_set)
    
    # 양쪽 종류 수 비교
    for i in range(len(topping) - 1):
        if left_counts[i] == right_counts[i + 1]:
            answer += 1
    
    return answer
"""
시간초과 슬라이싱 문제일듯
def solution(topping):
    answer = 0
    lt = len(topping)
    if lt % 2 == 1:
        return 0
    for i in range(lt):
        f = topping[:i]
        b = topping[i:]
        fs = list(set(f))
        bs = list(set(b))
        if len(fs) > len(bs):
            break
        if len(fs) == len(bs):
            answer += 1        
    return answer
"""