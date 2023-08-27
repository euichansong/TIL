t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    mx = 0
    # 하양의 범위는 0 ~ n-2 전까지
    for i in range(n-2):
        # 파랑의 범위는 i+1 부터 n-1 전까지
        for j in range(i+1, n-1):
            cnt = 0
            # 하양 나올수 있는 범위까지
            for s in range(i+1):
                cnt += arr[s].count('W')
            # 파랑 나올수 있는 범위 까지
            for s in range(i+1, j+1):
                cnt += arr[s].count('B')
            # 빨강 나올수 있는 범위 까지
            for s in range(j+1, n):
                cnt += arr[s].count('R')
            # 그중에 최대값 구한다
            # 그래야 빼서 최소값 나옴
            mx = max(mx,cnt)
    print(f'#{tc} {n*m - mx}')