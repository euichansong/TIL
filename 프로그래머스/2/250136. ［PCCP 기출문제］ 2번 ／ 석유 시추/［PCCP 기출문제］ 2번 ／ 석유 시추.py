"""
닿는거 다 걸리면 bfs? 
or 석유땅을 다 석유땅의 총 갯수로 바꾸고 열마다 내리면서 체크? 
n,m이 500이라 다 돌면 안되는데

한번이라도 찌르면 bfs 돌리고 석유땅 바꾸기? 
한번이라도 방문해서 크기를 구한 땅을 어떻게 체크하지

방문 tf 하나
찌른건 땅에 반영
하고 방문한적 있는건 방문땅을 다 크기로 변경

계산한적 있는 땅 따로 체크
방문한적 있으면 계산했다? 
방문 안했으면 크기 계산 후 석유량에 추가 
>> 복잡해

석유 덩어리의 가장 왼쪽 가장 오른쪽을 범위로해서 석유덩어리 크기를 저장한다 
"""
from collections import deque
def solution(land):
    n = len(land)
    m = len(land[0])
    col = [0] * m
    visit = [[0] * m for _ in range(n)]
    
    def bfs(si, sj):
        q = deque()
        q.append([si, sj])
        visit[si][sj] = 1
        cnt = 1
        le = sj
        ri = sj
        while q:
            ti, tj = q.popleft()
            # 가장작은 왼쪽값 
            le = min(le, tj)
            # 가장큰 오른쪽값
            ri = max(ri, tj)
            for ni, nj in [[ti, tj+1], [ti+1, tj], [ti-1, tj], [ti, tj-1]]:
                if 0 <= ni < n and 0 <= nj < m and land[ni][nj] == 1 and visit[ni][nj] == 0:
                    q.append([ni, nj])
                    visit[ni][nj] = 1
                    cnt += 1
        # 범위에 석유 넣기
        for t in range(le, ri + 1):
            col[t] += cnt

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visit[i][j] == 0:
                bfs(i, j)

    answer = max(col)
    return answer