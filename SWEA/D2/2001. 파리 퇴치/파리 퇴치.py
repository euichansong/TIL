t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_v = 0
    for i in range(n):
        for j in range(n):
            sum1 = 0
            for k in range(i, i+m):
                for q in range(j, j+m):
                    if 0<= k < n and 0<= q < n:
                        sum1 += arr[k][q]
            if max_v < sum1:
                max_v = sum1
    print(f'#{tc} {max_v}')