n, m, v = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
adj_m = [[0] * (n+1) for _ in range(n+1)]
st_b = v
st_d = v
for i in range(m):
    v1, v2 = arr[i][0], arr[i][1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

def dfs(v, adj_m):
    visited = [0] * (n + 1)
    stack = []

    visited[v] = 1
    print(v, end=' ')
    while True:
        for w in range(1, n+1):
            if adj_m[v][w] == 1 and visited[w] == 0:
                stack.append(v)
                v = w
                visited[w] = 1
                print(w, end=' ')
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

def bfs(st,adj_m):
    q = []
    visit = [0] * (n+1)
    q.append(st)
    visit[st] = 1
    while q:
        t = q.pop(0)
        print(t, end=' ')
        for w in range(1, n+1):
            if adj_m[t][w] == 1 and visit[w] == 0:
                q.append(w)
                visit[w] = visit[t] + 1

dfs(st_d, adj_m)
print()
bfs(st_b, adj_m)
