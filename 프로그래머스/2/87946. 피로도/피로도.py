answer = 0
def solution(k, dungeons):
    # print(k)
    global answer
    visited = [0] * len(dungeons)
    
    def jaegui (k, cnt, visited):
        global answer
        for i in range(len(dungeons)):
            if k >= dungeons[i][0] and visited[i] == 0:
                visited[i] = 1
                jaegui(k - dungeons[i][1], cnt + 1, visited)
                visited[i] = 0
        else:
            if cnt > answer:
                answer = cnt
            return
    jaegui(k,0,visited)
    return answer