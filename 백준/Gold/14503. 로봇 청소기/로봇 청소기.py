"""
0이면 빈칸
1이면 벽

북 동 남 서
0 1 2 3
"""
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
# 인덱스 맞춰서 좌표 제공
r,c,d = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(n)]
clean = [[0]*m for _ in range(n)]
ans = 0

def find_empty(r,c):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if 0<= nx < n and 0 <= ny < m:
            if room[nx][ny] == 0 and clean[nx][ny] == 0:
                return True
    return False

def move_back(r,c,d):
    # 북일때 남
    if d == 0:
        if room[r+1][c] == 0:
            return True
    # 동일때 서
    elif d == 1:
        if room[r][c-1] == 0:
            return True
    # 남일때 북
    elif d == 2:
        if room[r-1][c] == 0:
            return True            
    # 서일때 동
    elif d == 3:
        if room[r][c+1] == 0:
            return True
    return False

# def move_back(r,c,d):
#     back_d = (d + 2) % 4
#     # 북
#     if back_d == 0:
#         if room[r+1][c] == 0 and clean[r+1][c] == 0:
#             return True
#     # 동
#     elif back_d == 1:
#         if room[r][c-1] == 0 and clean[r][c-1] == 0:
#             return True
#     # 남
#     elif back_d == 2:
#         if room[r-1][c] == 0 and clean[r-1][c] == 0:
#             return True            
#     # 서
#     elif back_d == 3:
#         if room[r][c+1] == 0 and clean[r][c+1] == 0:
#             return True
#     return False



while True:
    if room[r][c] == 0 and clean[r][c] == 0:
        clean[r][c] = 1
        ans += 1
    if find_empty(r,c):
        # 빈칸 있는 경우
        d = (d + 3) % 4
        # 북
        if d == 0:
            if room[r-1][c] == 0 and clean[r-1][c] == 0:
                r -= 1
        # 동
        elif d == 1:
            if room[r][c+1] == 0 and clean[r][c+1] == 0:
                c += 1
        # 남
        elif d == 2:
            if room[r+1][c] == 0 and clean[r+1][c] == 0:
                r += 1
        # 서
        elif d == 3:
            if room[r][c-1] == 0 and clean[r][c-1] == 0:
                c -= 1
    else:
        # 빈칸 없는 경우
        if move_back(r,c,d):
            # 후진가능
            # 북
            if d == 0:
                r += 1
            # 동
            elif d == 1:
                c -= 1          
            # 남
            elif d == 2:
                r -= 1      
            # 서
            elif d == 3:
                c += 1    
        else:
            break
            
print(ans)
            
