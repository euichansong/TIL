
### 못품 못품 못품
n, m = map(int, input().split())
tree = list(map(int, input().split()))

tree.sort()
def bs(target, list):
    start = 1
    end = max(list)
    while start <= end:
        mid = (start + end) // 2
        tr = 0
        for i in list:
            # 같은건 안된다
            if i - mid > 0:
                tr += (i - mid)
        if tr < target:
            end = mid - 1
        elif tr > target:
            start = mid + 1
        if tr == target:
            return mid
print(bs(m,tree))
"""
2 10
3 9
"""