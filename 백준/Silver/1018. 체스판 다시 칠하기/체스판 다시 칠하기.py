n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
"""
0,0 보고 각 줄마다홀수 짝수 색깔 보고 다르면 카운트
같은 색깔 인덱스 >> 합이 홀수일때 짝수일때
0-1,3,5,7
1-0,2,4,6

0-0,2,4,6
1-1,3,5,7
"""

res = []
# 8칸 인덱스 에러 위해서
for i in range(n-7):
    # 8칸 인덱스 에러 위해서
    for j in range(m-7):
        # 맨앞이 w일때 카운트
        cntw = 0
        # 맨앞이 b일때 카운트
        cntb = 0
        # 8칸
        for r in range(i, i+8):
            # 8칸
            for w in range(j, j+8):
                # 행 열 합이 짝수인경우/ 맨 앞이 W 인 경우
                if (r+w) % 2 == 0:
                    # w가 아니라면 cntw +1
                    if matrix[r][w] != 'W':
                        cntw += 1
                    # b가 아니라면 cntb +1
                    elif matrix[r][w] != 'B':
                        cntb += 1
                # 행 열 합이 홀수인 경우/ 맨 앞이 b인 경우
                elif (r+w) % 2 == 1:
                    # w가 아니라면 cntb +1
                    if matrix[r][w] != 'W':
                        cntb += 1
                    # b가 아니라면 cntw +1
                    elif matrix[r][w] != 'B':
                        cntw += 1
        # 결과 리스트에 둘 중 최소값 넣음
        res.append(min(cntb,cntw))
# 그 중에 최소값 찾기
print(min(res))
