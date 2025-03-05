"""
테두리에 0으로 된 1줄 추가 
"""
from collections import deque

def solution(storage, requests):
    se = len(storage)
    ga = len(storage[0])
    # 0으로 둘러싸기
    new_storage = [[0]* (ga + 2) for _ in range(se+2)]
    for i in range(1,se+1):
        for j in range(1,ga+1):
            new_storage[i][j] = storage[i-1][j-1]
            
    # print(new_storage)
    # for i in range(se+2):
    #     print(new_storage[i])
    
    
    # 0,0에서 시작해서 들어갈 수 있는 컨테이너만 꺼낸다
    # 1번에 가능한 좌표들 미리 체크해두고 나중에 변경
    
    # def can_move(x,y):
    #     zero = []
    #     for nx,ny in [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]:
    #         if new_storage[nx][ny] == 0:
                
    def contain(req):
        word = req[0]
        if len(req) > 1:
            flag = True
        else:
            flag = False
        
        stay = deque()
        # 모든 컨테
        if flag:
            for i in range(se+2):
                for j in range(ga+2):
                    if new_storage[i][j] == word:
                        stay.append([i,j])
        # 접근 가능
        else:
            # choose = deque()
            # for i in range(se+2):
            #     for j in range(ga+2):
            #         if new_storage[i][j] == word:
            #             choose.append([i,j])
            # for nx,ny in choose:
                
                    
            q = deque()
            q.append([0,0])
            visited = [[0]* (ga + 2) for _ in range(se+2)]
            visited[0][0] = 1
            while q:
                px,py = q.popleft()                   
                for nx,ny in [[px+1,py],[px,py+1],[px-1,py],[px,py-1]]:
                    if 0<= nx < se+2 and 0<= ny < ga+2 and visited[nx][ny] == 0:
                        if new_storage[nx][ny]==0:
                            q.append([nx,ny])
                            visited[nx][ny] = 1
                        elif new_storage[nx][ny] == word:
                            stay.append([nx,ny])
                            
        if stay:
            while stay:
                px,py = stay.popleft()
                new_storage[px][py] = 0
                
                
    for i in requests:    
        contain(i)
        
    answer = 0
    for i in range(se+2):
        for j in range(ga+2):
            if new_storage[i][j] != 0:
                answer += 1
                
        
            
    
    return answer