import sys

n = int(sys.stdin.readline())


for _ in range(n):
    stack = []
    string = input()

    for i in string:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                stack.append('(')
                break
            else:
                stack.pop()

    if len(stack) != 0:
        print('NO')
    else:
        print('YES')