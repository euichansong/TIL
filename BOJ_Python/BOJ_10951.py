import sys
b =[]
for i in range(9):
    i = int(input())
    b.append(i)
print(max(b))
print(b.index(max(b)))
