"""
2 초	512 MB

문자의 갯수가 특정 갯수 이상 
길이는 주어진다

다 돌아야지 뭐
"""
from collections import deque
import sys
input = sys.stdin.readline

s,p = map(int,input().split())
dna = list(input())

# a,c,g,t 순서
need = list(map(int,input().split(" ")))
now = deque(dna[:p])
acnt = now.count('A')
ccnt = now.count('C')
gcnt = now.count('G')
tcnt = now.count('T')
ans = 0

if acnt >= need[0] and ccnt >= need[1] and gcnt >= need[2] and tcnt >= need[3]:
    ans += 1

# now 기준으로 맨앞에꺼 팝했는데 그게 acgt중에 하나면 그걸 acnt에서 숫자 빼고, 그 문자의 카운트를 늘린다. 
for i in range(p, s):
    left = now.popleft()
    if left == 'A':
        acnt -= 1
    elif left == 'C':
        ccnt -= 1
    elif left == 'G':
        gcnt -= 1
    elif left == 'T':
        tcnt -= 1

    right = dna[i]
    now.append(right)
    if right == 'A':
        acnt += 1
    elif right == 'C':
        ccnt += 1
    elif right == 'G':
        gcnt += 1
    elif right == 'T':
        tcnt += 1
    
    if acnt >= need[0] and ccnt >= need[1] and gcnt >= need[2] and tcnt >= need[3]:
        ans += 1

print(ans)