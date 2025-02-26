"""
2 초	128 MB

최대 랭킹 등수 p

1 1 20
2
"""
n,t,p = map(int, input().split())
if n == 0:
    print(1)
else:
    rank = list(map(int, input().split()))
    rank.append(t)
    rank.sort(reverse=True)
    ans = 1
    for i in rank:
        if i == t:
            break
        else:
            ans += 1
    if ans > p:
        print(-1)
    else:
        if len(rank) > p and t == rank[-1]:
            print(-1)
        else:
            print(ans)