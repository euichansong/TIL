T = int(input())
for _ in range(T):
    n = int(input())\
    # 내장함수 bin은 앞에 Ob가 붙기 때문에 index 2부터 출력
    b = bin(n)[2:]

    # b의 길이만큼 반복
    for i in range(len(b)):
        # 뒤에서부터 탐색
        # 1이 나오는 위치 찾기
        if b[::-1][i] == '1':
            # 공백을 두고 출력
            print(i, end=' ')