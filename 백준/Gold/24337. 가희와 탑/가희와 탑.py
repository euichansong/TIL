"""
1 초	512 MB

사전순

1 ≤ N ≤ 100000

가희기준부터 세우고 단비기준? 섞어쓰는거 가능한가
> 불가능 사전순이니까

5 3 3
1 2 3 2 1

건물보이는거 합쳐서 건물+2 이상이면 불가능 1까진 가능
>볼 수 있는 건물이 최대 숫자

5 2 2
1 1 1 2 1

5 1 3
3 1 1 2 1

6 4 3
123421

6 3 4
124321

# 7 4 3 인경우

a,b중 크거나 같은숫자 기준으로 for문 돌리고
now a = [1,2,3,4] 
now b= [1,2] 
now= [1]* n-(a+b) + 1
> b는 이미 큰 숫자가 a에 있기때문에 1 빼고 for문 돌린다
now + nowa + reverse_nowb
1 1 2 3 4 2 1
이렇게 리스트가 더해지면 정답

b가 더 큰경우는?
> a,b중 큰숫자 for 문 돌리고 실제로 b가 더 클땐 a를 reverse 해서 합친다
> now + nowb + reverse_nowa

# 7 3 4
nowa = [1,2,3,4]
nowb = [1,2]
now = [1]
1 1 2 4 3 2 1
"""
# 건물갯수, 가희건물, 단비건물
n,a,b = map(int, input().split())

if a+b-1 > n:
    print(-1)
else:
    if a >= b:
        nowa = [0]*a
        for i in range(len(nowa)):
            nowa[i] = i+1
        nowb = [0] * (b-1)
        for i in range(len(nowb)):
            nowb[i] = i+1
        core = nowa + nowb[::-1]
    else:
        nowa = [0] * (a-1)
        for i in range(len(nowa)):
            nowa[i] = i+1
        nowb = [0] * b
        for i in range(len(nowb)):
            nowb[i] = i+1
        core = nowa + nowb[::-1]

    now = [1] * (n - (a+b) + 1)
    # a가 1이면 맨앞이 가장 큰 건물이어야 한다 
    # 5 1 3 >> 3 1 1 2 1 이렇게
    if a == 1:
        ans = [core[0]] + now + core[1:]
    else:
        ans = now + core
    print(*(ans))





