"""
3*3 행렬을 뒤집는것

1번쨰
0111
0101
0111

2번째
1001
1011
1001


"""
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
amat = [list(input().rstrip()) for _ in range(n)]
bmat = [list(input().rstrip()) for _ in range(n)]
def change(mat,sx,sy):
    cnt = 0
    for i in range(sx,sx+3):
        for j in range(sy,sy+3):
            if mat[i][j] == '0':
                mat[i][j] = '1'
                cnt += 1
            else:
                mat[i][j] = '0'
                cnt += 1


ans = 0
flag = True
if n < 3 or m < 3:
    ans = -1
else:
    for i in range(n-2):
        if flag:

            for j in range(m-2):
                if amat[i][j] != bmat[i][j]:
                    change(amat,i,j)
                    ans += 1
                if amat == bmat:
                    flag = False
                    break
        else:
            break
                # for p in amat:
                #     print(p)
                # print('==============')

# print(ans,"same")
if n< 3 or m < 3:
    if amat == bmat:
        ans = 0
        
if amat != bmat:
    ans = -1

print(ans)
