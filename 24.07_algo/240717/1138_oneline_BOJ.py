"""
키가 1인사람부터
왼쪽에 자기보다 큰 사람이 있는지 확인

첫번째 1은 리스트의 인덱스값
마지막 값은 당연히 0이지
2번이 왼쪽에 1개 있다는 뜻은
1옆에 붙어있다는 뜻?
다 1로 바꾸고 다 2로 바꾸고

왼쪽에 큰사람 0인데 라인 끝 아니면
"""
n = int(input())
line = list(map(int, input().split()))
asc = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        # 왼쪽에 자기보다 큰 인원수 만큼 빈자리 카운트 한다
        # 해당 위치 비어있으면 넣는다
        if cnt == line[i] and asc[j] == 0:
            asc[j] = i + 1
            break
        # 해당 위치 비어있으면 빈자리 카운트 증가

        # 비어있지 않다면 자기보다 작은 숫자라는 뜻
        # 이게 계속 이해가 안됬던 부분
        elif asc[j] == 0:
            cnt += 1
print(*asc)


