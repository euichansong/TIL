"""
재귀인데 어캐 하지?

"""
cnt = 0
def solution(numbers, target):
    global cnt
    answer = 0
    recursion(numbers,target, 0, 0)
    answer = cnt
    return answer

def recursion(numbers,target, result, idx):
    global cnt
    if idx == len(numbers):
        if result == target:
            cnt += 1
            print(cnt)
        return
    else:
        recursion(numbers,target, result-numbers[idx],idx+1)
        recursion(numbers,target, result+numbers[idx],idx+1)
                