# 1부터 n까지 자연수중 중복없이 m개 고르는 순열
n, m = map(int, input().split())
arr = []


# 백트레킹 함수
def n_and_m(s, n, m):
    # arr 의 길이가 m이 되면 출력
    if len(arr) == m:
        print(*arr)
        return
    # 시작값 부터 n까지 범위
    for j in range(s, n+1):
        # 중복값이 없도록 not in 사용
        if j not in arr:
            # j값 저장
            arr.append(j)
            # j+1 을 시작점으로 하는 백트레킹
            n_and_m(j+1, n, m)
            # 재귀 끝나면 넣은 값 제거
            arr.pop()
# 함수 시작
n_and_m(1, n, m)