n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))
# #  풀이 1번
# # 시간초과 때문에 set으로 중복 제거
# nlist = set(nlist)
# for i in mlist:
#     if i in nlist:
#         print(1)
#     else:
#         print(0)

# 풀이 2번
def BinarySearch(list,target):
    # 시작 인덱스
    start = 0
    # 끝 인덱스 인덱스값이기 때문에 -1
    last = len(list)-1
    # 시작인덱스가 끝 인덱스보다 작거나 같을때 까지
    while start <= last:
        # 중간 인덱스 계산
        middle = (start + last) // 2
        # 중간인덱스값이 타겟보다 크면 타겟은 중간값 왼쪽에 있어야 한다
        if list[middle] > target:
            # 중간인덱스 -1 이 새로운 끝 인덱스값
            last = middle - 1
        # 중간인덱스값이 타겟보다 작으면 타겟은 중간값 오른쪽에 있어야 한다
        elif list[middle] < target:
            # 중간인덱스 + 1 이 새로운 시작 인덱스값
            start = middle + 1
        # 찾으면 True
        else:
            return True
    # 못찾으면 False
    return False

# 이진 탐색 하려면 정렬 해야 한다
nlist.sort()
for i in mlist:
    if BinarySearch(nlist, i):
        print(1)
    else:
        print(0)
