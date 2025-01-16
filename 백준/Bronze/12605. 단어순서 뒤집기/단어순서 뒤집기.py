t = int(input())
for tt in range(1,t+1):
    word = list(input().split())
    ans = []
    for i in range(len(word)-1,-1,-1):
        ans.append(word[i])
    all = ' '.join(map(str,ans))
    # print(all)
    print(f'Case #{tt}: {all}')