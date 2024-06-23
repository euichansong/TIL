# def sol(n, times):
#     answer = 0
#     times.sort()
#     t = 0
#     # # 완탐 >> 시간초과
#     # while n > 0:
#     #     while True:
#     #         t += 1
#     #         break
#     #     for time in times:
#     #         if t % time == 0:
#     #             n -= 1
#     #     print(n)
#     # print(t)
#     # return t
#     multi = 2
#     while len(times) < n-1:
#         for i in times:
#             add_time = i * multi
#             times.append(add_time)
#
#             if len(times) >= n - 2:
#                 break
#         multi += 1
#     print(times)
#
#     return answer
def solutio(n, times):
    times.sort()
    answer = 0

    def Binary_Search(n, times):
        # 시작점
        start = times[0]
        # 끝점 최소시간 * 명수 가 최대값이다
        end = times[0] * n
        while True:
            # 중간값
            mid = (start + end) // 2
            # 명수 계산용 카운트
            cnt = 0
            # 중간값 / 시간 하면 심사대 당 심사 명수 나온다
            for i in times:
                cnt += (mid // i)
            if cnt >= n:
                end = mid
            elif cnt < n:
                start = mid
            # 왜 -1 안하면 무한루프일까
            if start == end - 1:
                return end

    answer = Binary_Search(n, times)
    return answer


num = int(input())

print(solutio(num,[7,10]))
