# 1부터 n까지 자연수중 중복없이 m개 고르는 순열
n, m = map(int, input().split())
arr = [q for q in range(1, n+1)]


# 백트레킹 함수
def n_and_m(i, n, m):
    # 시작값이 m 값이 되면 출력, 카운트 증가
    if i == m:
        print(*pick)
        return
    else:
        # 0~n-1까지 인덱스
        for j in range(n):
            # 방문하지 않았으면
            if visited[j] == 0:
                # 방문하지 않은 인덱스를 고름
                pick[i] = arr[j]
                # 방문처리
                visited[j] = 1
                # 다음 값 처리
                n_and_m(i+1, n, m)
                # 백트레킹 끝나고 복귀
                visited[j] = 0
# 방문 표시 함수
visited = [0] * n
# 고른 순열
pick = [0] * m
# 함수 시작
n_and_m(0, n, m)

# 중복은 제거하는(뒤집어도 같으면 제거)비트연산으로 뽑는 순열
# result = []
# for i in range(1 << n):
#     res = []
#     for j in range(n):
#         if i & (1 << j):
#             res.append(arr[j])
#     # if len(res) == m:
#     if res:
#         result.append(res)
# result.sort(key=lambda x:x[0])
# for i in result:
#     if len(i) == m:
#         print(i)

