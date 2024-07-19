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
        elif asc[j] == 0:
            cnt += 1
print(*asc)