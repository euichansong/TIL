"""
재귀인데 어캐 하지?

"""
cnt = 0
def solution(numbers, target):
    answer = 0
    recursion(numbers, target, 0, 0)
    return answer


def recursion(numbers, target, result, idx):
    global cnt
    if result == target:
        cnt += 1
        return
    elif idx >= len(numbers):
        return
    else:
        for i in numbers[idx:]:
            recursion(numbers, target, result - i, idx + 1)
            recursion(numbers, target, result + i, idx + 1)
numbers = [1, 1, 1, 1, 1]
target = 3
solution(numbers,target)
print(cnt)