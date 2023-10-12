import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def cal(num_idx, sum):
    global min_sum, max_sum
    if num_idx == n-1:
        max_sum = max(max_sum, sum)
        min_sum = min(min_sum, sum)
        return
    for op in range(4):
        if oper_list[op] > 0:
            oper_list[op] -= 1
            if op == 0:
                new_sum = sum + num_list[num_idx+1]
            if op == 1:
                new_sum = sum - num_list[num_idx+1]
            if op == 2:
                new_sum = sum * num_list[num_idx+1]
            if op == 3:
                new_sum = sum / num_list[num_idx+1]
                new_sum = int(new_sum)
            cal(num_idx+1, new_sum)
            oper_list[op] += 1


n = int(input())
num_list = list(map(int, input().split()))
oper_list = list(map(int, input().split()))
min_sum = 1000000000
max_sum = -1000000000
cal(0, num_list[0])
print(max_sum)
print(min_sum)