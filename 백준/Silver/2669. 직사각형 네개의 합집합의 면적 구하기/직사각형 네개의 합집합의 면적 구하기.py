matrix = [[0] * 101 for _ in range(101)]

for tt in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] = 1
cnt = 0
for q in range(101):
    for w in range(101):
        if matrix[q][w] == 1:
            cnt += 1
print(cnt)