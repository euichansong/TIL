import sys
input = sys.stdin.readline

n, game = input().split()
n = int(n)
namedict = {}
cnt = 1
for i in range(n):
    name = input().rstrip()
    if name in namedict:
        cnt += 1
        namedict[name] = cnt
    else:
        namedict[name] = 1

# print(namedict)
# print(len(namedict))
# 의미 없음 문제 잘읽을것 한번 같이 플레이 하면 다시 플레이 안함
# sortdict = sorted(namedict.items(), key=lambda x: x[1], reverse=True)
# print(sortdict)
if game == 'Y':
    print(len(namedict)//1)
elif game == 'F':
    print(len(namedict)//2)
elif game == 'O':
    print(len(namedict)//3)