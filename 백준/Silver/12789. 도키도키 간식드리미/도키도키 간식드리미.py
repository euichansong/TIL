import sys
input =sys.stdin.readline
N = int(input())
lst = list(map(int,input().split()))
stack = []
start = 1

while lst or stack:
    if stack and stack[-1] == start:
        start+=1
        stack.pop()
        continue
    elif lst:
        now = lst.pop(0)
        stack.append(now)
    else:
        break

if start == N+1:
    print("Nice")

else:
    print("Sad")