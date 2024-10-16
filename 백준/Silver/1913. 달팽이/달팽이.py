import sys
input = sys.stdin.readline
n = int(input())
need = int(input())
arr = [[0] * n for _ in range(n)]

nowx = n // 2
nowy = n // 2
sn = 1
fn = n ** 2
d = 0

use = 1
next_use = 1
nu = False

while sn <= fn:
    arr[nowx][nowy] = sn
    
    if d == 0:
        nowx -= 1
    elif d == 1:
        nowy += 1
    elif d == 2:
        nowx += 1
    elif d == 3:
        nowy -= 1
    
    use -= 1
    
    if use == 0:
        if nu:
            next_use += 1
        use = next_use
        d = (d + 1) % 4
        nu = not nu
    
    sn += 1

for row in arr:
    print(" ".join(map(str, row)))
for i in range(n):
    for j in range(n):
        if arr[i][j] == need:
            print(i+1,j+1)
