# def solution(phone_book):
#     answer = True
#     dict = {}
#     pb = len(phone_book)
#     h = phone_book[0]
#     lh = len(h)
#     flag = False
#     for i in range(1,pb):
#         if flag:
#             break
#         cnt = 0
#         for j in range(lh):
#             if phone_book[i][j] == h[j]:
#                 cnt += 1
#             if cnt == lh:
#                 answer = False
#                 flag = True
#                 break
#     return answer
def solution(phone_book):
    answer = True
    # 문자열 정렬
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    return answer