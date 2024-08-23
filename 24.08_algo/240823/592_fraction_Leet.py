"""
ㅅㅂ 10은 생각을 못했네

이건 그냥 구현임 ㅈ같은

/다음은 무조건 분모 그 다음은 무조건 계산 기호
-다음은 무조건 분자 / 분모
+ 다음은 무조건 분자 / 분모

>>> /기호 나올때까지 문자열 만듬

제공 문자열 숫자도 문자열

-면 continue 하고 플래그?
"""

class Solution:
    def fractionAddition(self, expression: str) -> str:
        exp = list(expression)

        minus = True
        total = 1
        fraclist = []
        idx = 0
        strnum = ''
        son = 0
        mother = 0

        while idx < len(exp):
            # 숫자 나올때 까지
            while exp[idx].isdigit():
                strnum += exp[idx]
                idx += 1
                # 마지막 숫자
                if idx == len(exp):
                    break
            # 기호면
            else:
                if exp[idx] == '/':
                    if minus:
                        son += int(strnum)
                        idx += 1
                        strnum = ''
                        continue
                    else:
                        son -= int(strnum)
                        idx += 1
                        strnum = ''
                        continue

                if exp[idx] == '-':
                    minus = False
                    if strnum:
                        while exp[idx].isdigit():
                            strnum += exp[idx]
                            idx += 1
                        mother += int(strnum)
                        total *= mother
                        fraclist.append([son, mother])
                        strnum = ''
                        mother = 0
                        son = 0
                    else:
                        idx += 1
                        continue

                elif exp[idx] == '+':
                    minus = True
                    while exp[idx].isdigit():
                        strnum += exp[idx]
                        idx += 1
                    mother += int(strnum)
                    total *= mother
                    fraclist.append([son, mother])
                    strnum = ''
                    mother = 0
                    son = 0
                    idx += 1
                    continue
        # 마지막 숫자 계산 해주기
        mother = int(strnum)
        total *= mother
        fraclist.append([son, mother])

        # 통분한 분자 / total 은 통분한 분모
        totalson = 0
        for j in range(len(fraclist)):
            totalson += int(fraclist[j][0] * (total / fraclist[j][1]))

        answer = ''

        # 최대 공약수 구하는 함수
        def cdg(totalson, total):
            cdgys = 1
            for y in range(1, total + 1):
                # 둘다 나눴을때 나머지가 0이면 공약수
                if (totalson % y == 0) and (total % y == 0):
                    # 최대 공약수 갱신
                    cdgys = y
            return cdgys

        # 총합 0이면 그냥 0
        if totalson == 0:
            answer = "0/1"
        else:
            cdgys = cdg(abs(totalson), total)
            answer += str(int(totalson / cdgys))
            answer += '/'
            answer += str(int(total / cdgys))
        return answer

# 실패작


# class Solution:
#     def fractionAddition(self, expression: str) -> str:
#         exp = list(expression)
#         minus = True
#         total = 1
#         fraclist = []
#         for i in range(len(exp)):
#             son = 0
#             mother = 0
#             if exp[i] == '-':
#                 minus = False
#                 continue
#             if exp[i] == '/':
#                 if minus:
#                     if exp[i-1] == '0':
#                         son += 10
#                         if exp[i+1] == '0':
#                         mother += int(exp[i+1])
#                         total *= mother
#                     else:
#                         son += int(exp[i-1])
#                         mother += int(exp[i+1])
#                         total *= mother
#                 else:
#                     if exp[i-1] == '0':
#                         son -= 10
#                         mother += int(exp[i+1])
#                         total *= mother
#                     else:
#                         son += int(exp[i-1])
#                         mother += int(exp[i+1])
#                         total *= mother

#                 fraclist.append([son,mother])
#                 minus = True

#         totalson = 0
#         for j in range(len(fraclist)):
#             totalson += int(fraclist[j][0]*(total / fraclist[j][1]))

#         answer = ''

#         """
#         약분이 안된다는건 뭐지?
#         >>> 서로 최대공약수로 나눈것
#         """

#         def cdg(totalson,total):
#             cdgys = 1
#             for y in range(1,total+1):
#                 if (totalson % y == 0) and (total % y == 0):
#                     cdgys = y
#             return cdgys

#         if totalson == 0:
#             answer = "0/1"
#         else:
#             if totalson >= 0:
#                 cdgys = cdg(totalson,total)
#                 answer += str(int(totalson/cdgys))
#                 answer += '/'
#                 answer += str(int(total/cdgys))

#             else:
#                 cdgys = cdg(abs(totalson),total)
#                 answer += str(int(totalson/cdgys))
#                 answer += '/'
#                 answer += str(int(total/cdgys))
#         return answer
