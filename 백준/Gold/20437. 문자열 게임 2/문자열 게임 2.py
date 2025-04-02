"""
1 초	1024 MB
짧은거 하나 긴거 하나 없으면 -1
"""
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    word = input().rstrip()
    k = int(input().rstrip())
    mi = 10001
    ma = -1
    for i in range(len(word)):
        if word[i:].count(word[i]) < k:
            continue 
        cnt = 0
        for j in range(i, len(word)):
            if word[j] == word[i]:
                cnt += 1
            if cnt == k:
                mi = min(mi, j - i + 1)
                ma = max(ma, j - i + 1)
                break

    if ma == -1:
        print(-1)
    else:
        print(mi, ma)

    #     for j in range(i+1,len(word)):
    #         if word[i] == word[j]:
    #             cnt += 1
    #         if cnt == count:
    #             mi = min(mi,j-i+1)
    #             ma = max(ma,j-i+1)
    #             break
