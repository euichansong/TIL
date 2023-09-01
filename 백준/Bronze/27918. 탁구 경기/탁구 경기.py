n = int(input())
dal = 0
po = 0
for i in range(n):
    a = input()
    if a == 'D':
        dal += 1
    else:
        po += 1
    if abs(dal-po) == 2:
        break
print(f'{dal}:{po}')